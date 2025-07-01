from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        NextEnergyPriceSensor(coordinator, "electricity"),
        NextEnergyPriceSensor(coordinator, "gas"),
        NextEnergyPriceTrendSensor(coordinator),
    ])

class NextEnergyPriceSensor(SensorEntity):
    def __init__(self, coordinator, sensor_type):
        self.coordinator = coordinator
        self.type = sensor_type
        self._attr_name = f"NextEnergy {sensor_type.capitalize()} Price"
        self._attr_unique_id = f"nextenergy_{sensor_type}_price"

    @property
    def state(self):
        data = self.coordinator.data or {}
        return data.get(f"{self.type}_price")

    @property
    def unit_of_measurement(self):
        return "€/kWh" if self.type == "electricity" else "€/m³"

class NextEnergyPriceTrendSensor(SensorEntity):
    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_name = "NextEnergy Price Trend"
        self._attr_unique_id = "nextenergy_price_trend"

    @property
    def state(self):
        data = self.coordinator.data or {}
        return data.get("price_trend", "unknown")
