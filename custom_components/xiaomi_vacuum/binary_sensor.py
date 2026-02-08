"""Support for Xiaomi Vacuum Binary Sensors."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
    BinarySensorDeviceClass,
)
from homeassistant.config_entries import ConfigEntry

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

from .coordinator import XiaomiVacuumDataUpdateCoordinator
from .entity import XiaomiVacuumEntity, XiaomiVacuumEntityDescription


@dataclass
class XiaomiVacuumBinarySensorEntityDescription(XiaomiVacuumEntityDescription, BinarySensorEntityDescription):
    """Describes Xiaomi Vacuum BinarySensor entity."""


BINARY_SENSORS: tuple[BinarySensorEntityDescription, ...] = (
    ## This entity is need for battery icon to be rendered correctly since vacuum entity attr_charging attribute has been deprecated
    XiaomiVacuumBinarySensorEntityDescription(
        key="charging_state",
        name="Charging State",
        device_class=BinarySensorDeviceClass.BATTERY_CHARGING,
        icon_fn=lambda value, device: (
            "mdi:power-plug-battery"
            if device.status.charging
            else "mdi:power-plug-off" if not device.status.docked else "mdi:power-plug"
        ),
        value_fn=lambda value, device: device.status.charging,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Xiaomi Vacuum Binary Sensor based on a config entry."""
    coordinator: XiaomiVacuumDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        XiaomiVacuumBinarySensorEntity(coordinator, description)
        for description in BINARY_SENSORS
        if description.exists_fn(description, coordinator.device)
    )


class XiaomiVacuumBinarySensorEntity(XiaomiVacuumEntity, BinarySensorEntity):
    """Defines a Xiaomi Vacuum Binary Sensor entity."""

    def __init__(
        self,
        coordinator: XiaomiVacuumDataUpdateCoordinator,
        description: XiaomiVacuumBinarySensorEntityDescription,
    ) -> None:
        """Initialize a Xiaomi Vacuum BinarySensor entity."""
        super().__init__(coordinator, description)

    @property
    def is_on(self) -> bool | None:
        """Return value of binary sensor."""
        value = None
        if self.entity_description.property_key is not None:
            value = self.device.get_property(self.entity_description.property_key)
        if self.entity_description.value_fn is not None:
            return bool(self.entity_description.value_fn(value, self.device))
        return bool(value)
