from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import NextEnergyAPI
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL

class NextEnergyDataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, config_entry):
        self.api = NextEnergyAPI(
            hass,
            config_entry.data["username"],
            config_entry.data["password"]
        )
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_UPDATE_INTERVAL),
        )

    async def _async_update_data(self):
        try:
            return await self.api.fetch_prices()
        except Exception as err:
            raise UpdateFailed(f"Error fetching NextEnergy data: {err}")
