"""Support for Xiaomi Vacuum numbers."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.number import (
    NumberEntity,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import entity_platform

from .const import DOMAIN, UNIT_MINUTES

from .coordinator import XiaomiVacuumDataUpdateCoordinator
from .entity import XiaomiVacuumEntity, XiaomiVacuumEntityDescription
from .xiaomi import XiaomiVacuumAction, XiaomiVacuumProperty


@dataclass
class XiaomiVacuumNumberEntityDescription(XiaomiVacuumEntityDescription, NumberEntityDescription):
    """Describes Xiaomi Vacuum Number entity."""

    mode: NumberMode = NumberMode.AUTO
    post_action: XiaomiVacuumAction = None


NUMBERS: tuple[XiaomiVacuumNumberEntityDescription, ...] = (
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.VOLUME,
        icon_fn=lambda value, device: "mdi:volume-off" if value == 0 else "mdi:volume-high",
        mode=NumberMode.SLIDER,
        native_min_value=0,
        native_max_value=100,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        post_action=XiaomiVacuumAction.TEST_SOUND,
    ),
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.MOP_CLEANING_REMAINDER,
        icon="mdi:alarm-check",
        mode=NumberMode.BOX,
        native_unit_of_measurement=UNIT_MINUTES,
        native_min_value=0,
        native_max_value=180,
        native_step=15,
        entity_category=EntityCategory.CONFIG,
    ),
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.DND_START,
        key="dnd_start_hour",
        icon="mdi:clock-start",
        mode=NumberMode.BOX,
        native_min_value=0,
        native_max_value=23,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        value_fn=lambda value, device: value.split(":")[0],
        format_fn=lambda value, device: "{:02d}:".format(value) + device.status.dnd_start.split(":")[1],
        entity_registry_enabled_default=False,
    ),
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.DND_START,
        key="dnd_start_minute",
        icon="mdi:clock-start",
        mode=NumberMode.BOX,
        native_min_value=0,
        native_max_value=59,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        value_fn=lambda value, device: value.split(":")[1],
        format_fn=lambda value, device: device.status.dnd_start.split(":")[0] + ":{:02d}".format(value),
        entity_registry_enabled_default=False,
    ),
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.DND_END,
        key="dnd_end_hour",
        icon="mdi:clock-end",
        mode=NumberMode.BOX,
        native_min_value=0,
        native_max_value=23,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        value_fn=lambda value, device: value.split(":")[0],
        format_fn=lambda value, device: "{:02d}:".format(value) + device.status.dnd_end.split(":")[1],
        entity_registry_enabled_default=False,
    ),
    XiaomiVacuumNumberEntityDescription(
        property_key=XiaomiVacuumProperty.DND_END,
        key="dnd_end_minute",
        icon="mdi:clock-end",
        mode=NumberMode.BOX,
        native_min_value=0,
        native_max_value=59,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        value_fn=lambda value, device: value.split(":")[1],
        format_fn=lambda value, device: device.status.dnd_end.split(":")[0] + ":{:02d}".format(value),
        entity_registry_enabled_default=False,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Xiaomi Vacuum number based on a config entry."""
    coordinator: XiaomiVacuumDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        XiaomiVacuumNumberEntity(coordinator, description)
        for description in NUMBERS
        if description.exists_fn(description, coordinator.device)
    )


class XiaomiVacuumNumberEntity(XiaomiVacuumEntity, NumberEntity):
    """Defines a Xiaomi Vacuum number."""

    def __init__(
        self,
        coordinator: XiaomiVacuumDataUpdateCoordinator,
        description: XiaomiVacuumNumberEntityDescription,
    ) -> None:
        """Initialize Xiaomi Vacuum ."""
        super().__init__(coordinator, description)
        self._attr_mode = description.mode
        self._attr_native_value = super().native_value

    @callback
    def _handle_coordinator_update(self) -> None:
        self._attr_native_value = super().native_value
        super()._handle_coordinator_update()

    async def async_set_native_value(self, value: float) -> None:
        """Set the Xiaomi Vacuum number value."""
        if not self.available:
            raise HomeAssistantError("Entity unavailable")

        value = int(value)
        if self.entity_description.format_fn is not None:
            value = self.entity_description.format_fn(value, self.device)

        if value is None:
            raise HomeAssistantError("Invalid value")

        if await self._try_command(
            "Unable to call %s",
            self.device.set_property,
            self.entity_description.property_key,
            value,
        ):
            if self.entity_description.post_action is not None:
                await self._try_command(
                    "Unable to call %s",
                    self.device.call_action,
                    self.entity_description.post_action,
                )

    @property
    def native_value(self) -> int | None:
        """Return the current Xiaomi Vacuum number value."""
        return self._attr_native_value
