from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        NextEnergyPriceSensor(coordinator, "current_market"),
        NextEnergyPriceSensor(coordinator, "current_market_plus"),
        NextEnergyPriceSensor(coordinator, "next_market"),
        NextEnergyPriceSensor(coordinator, "next_market_plus"),
    ])

class NextEnergyPriceSensor(SensorEntity):
    def __init__(self, coordinator, key):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = f"NextEnergy {key.replace('_', ' ').title()}"
        self._attr_unique_id = f"nextenergy_{key}"

    @property
    def state(self):
        data = self.coordinator.data or {}
        return round(data.get(self.key, 0), 4)

    @property
    def unit_of_measurement(self):
        return "€/kWh"

    @property
    def available(self):
        return self.coordinator.last_update_success
