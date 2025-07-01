import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import NextEnergyAPI
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)

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
            prices = await self.api.fetch_prices()
            if not prices:
                raise Exception("No price data returned from API.")
            # Store last/next hour for sensors
            from datetime import datetime
            now = datetime.now().replace(minute=0, second=0, microsecond=0)
            current = next((p for p in prices if p["hour"].startswith(now.strftime('%Y-%m-%dT%H'))), prices[0])
            next_hour = next((p for p in prices if p["hour"].startswith((now + timedelta(hours=1)).strftime('%Y-%m-%dT%H'))), prices[1] if len(prices) > 1 else prices[0])
            return {
                "current_market": current["market"],
                "current_market_plus": current["market_plus"],
                "next_market": next_hour["market"],
                "next_market_plus": next_hour["market_plus"],
                "all_prices": prices,
            }
        except Exception as err:
            raise UpdateFailed(f"Error fetching NextEnergy data: {err}")
