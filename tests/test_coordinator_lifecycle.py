"""Coordinator lifecycle tests: update errors reported after teardown.

Stdlib unittest against a real HomeAssistant core and a fake device, so no
network or Xiaomi account is involved. Run with Home Assistant and the
integration requirements installed, from the repository root:

    python -m unittest discover -s tests
"""

import asyncio
import os
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from homeassistant.core import HomeAssistant  # noqa: E402
from homeassistant.helpers import frame  # noqa: E402
from homeassistant.helpers.update_coordinator import UpdateFailed  # noqa: E402

from custom_components.xiaomi_vacuum import async_unload_entry  # noqa: E402
from custom_components.xiaomi_vacuum import coordinator as coordinator_module  # noqa: E402
from custom_components.xiaomi_vacuum.const import CONF_DONATED, CONF_VERSION, DOMAIN  # noqa: E402
from custom_components.xiaomi_vacuum.xiaomi import VERSION  # noqa: E402
from custom_components.xiaomi_vacuum.xiaomi.exceptions import DeviceException  # noqa: E402


class FakeDevice:
    """The XiaomiVacuumDevice surface the coordinator uses, without I/O."""

    def __init__(self, name, host, token, *args):
        self.name = name
        self.host = host
        self.token = token
        self.mac = "00:00:00:00:00:00"
        self.available = False
        self.disconnected = False
        self.auth_failed = False
        self.status = SimpleNamespace(has_temporary_map=False)
        self._protocol = SimpleNamespace(cloud=None)
        self.update_error = None
        self.update_callback = None
        self.error_callback = None

    def listen(self, callback, property=None):
        if callback is None:
            self.update_callback = None
        elif property is None:
            self.update_callback = callback

    def listen_error(self, callback):
        self.error_callback = callback

    def update(self):
        if self.update_error:
            raise self.update_error
        self.available = True

    def schedule_update(self, wait=None):
        pass

    def disconnect(self):
        self.disconnected = True

    def fail_from_update_thread(self, ex):
        """What XiaomiVacuumDevice._update_task does after the 4th failed retry."""
        self.available = False
        if self.error_callback:
            self.error_callback(ex)


class CoordinatorLifecycleTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.loop_errors = []
        asyncio.get_running_loop().set_exception_handler(lambda loop, ctx: self.loop_errors.append(ctx))
        self.hass = HomeAssistant(tempfile.mkdtemp())
        frame.async_setup(self.hass)
        self.entry = SimpleNamespace(
            entry_id="test-entry",
            data={"name": "Vacuum", "host": "192.0.2.1", "token": "0" * 32},
            options={CONF_VERSION: VERSION, CONF_DONATED: True},
        )
        patcher = patch.object(coordinator_module, "XiaomiVacuumDevice", FakeDevice)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.coordinator = coordinator_module.XiaomiVacuumDataUpdateCoordinator(self.hass, entry=self.entry)
        self.device = self.coordinator.device

    async def _drain_loop(self):
        for _ in range(3):
            await asyncio.sleep(0)

    async def _report_error_from_update_thread(self):
        ex = DeviceException("Unable to discover the device over cloud")
        await asyncio.get_running_loop().run_in_executor(None, self.device.fail_from_update_thread, ex)
        await self._drain_loop()

    async def test_successful_update_then_error_marks_coordinator_failed(self):
        self.assertIs(await self.coordinator._async_update_data(), self.device)
        self.assertTrue(self.coordinator.last_update_success)

        await self._report_error_from_update_thread()

        self.assertEqual(self.loop_errors, [])
        self.assertFalse(self.coordinator.last_update_success)
        self.assertIsInstance(self.coordinator.last_exception, DeviceException)

        self.device.available = True
        self.coordinator.async_set_updated_data(self.device)
        self.assertTrue(self.coordinator.last_update_success)

    async def test_update_error_after_unload_is_ignored(self):
        await self.coordinator._async_update_data()
        self.hass.data[DOMAIN] = {self.entry.entry_id: self.coordinator}

        self.hass.config_entries = SimpleNamespace(async_unload_platforms=AsyncMock(return_value=True))
        self.assertTrue(await async_unload_entry(self.hass, self.entry))

        await self._report_error_from_update_thread()
        self.assertEqual(self.loop_errors, [])
        self.assertIsNone(self.coordinator.device)

    async def test_update_error_after_failed_setup_is_ignored(self):
        self.device.update_error = DeviceException("Unable to discover the device over cloud")
        self.coordinator._available = True  # previous run had been available

        with self.assertRaises(UpdateFailed):
            await self.coordinator._async_update_data()

        await self._report_error_from_update_thread()
        self.assertEqual(self.loop_errors, [])

    async def test_callbacks_queued_before_teardown_are_ignored(self):
        await self.coordinator._async_update_data()
        self.coordinator.device = None

        self.coordinator.async_set_update_error(DeviceException("late"))
        self.coordinator.async_set_updated_data(None)
        await self._drain_loop()
        self.assertEqual(self.loop_errors, [])


if __name__ == "__main__":
    unittest.main()
