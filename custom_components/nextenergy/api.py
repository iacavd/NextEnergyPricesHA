import logging
from homeassistant.helpers import aiohttp_client
from .const import API_URL

_LOGGER = logging.getLogger(__name__)

class NextEnergyAPI:
    def __init__(self, hass, username, password):
        self.hass = hass
        self.username = username
        self.password = password

    async def fetch_prices(self):
        session = aiohttp_client.async_get_clientsession(self.hass)
        payload = {"username": self.username, "password": self.password}
        async with session.post(API_URL, json=payload) as resp:
            if resp.status != 200:
                _LOGGER.error("API error: %s", resp.status)
                raise Exception(f"API error: {resp.status}")
            data = await resp.json()
            # Expecting data in form: {"prices": [{"hour": "2025-07-02T00:00:00", "market": 0.11, "market_plus": 0.23}, ...]}
            return data.get("prices", [])
