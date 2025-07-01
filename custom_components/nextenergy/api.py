import aiohttp
from homeassistant.helpers import aiohttp_client
from .const import API_URL

class NextEnergyAPI:
    def __init__(self, hass, username, password):
        self.hass = hass
        self.username = username
        self.password = password

    async def fetch_prices(self):
        session = aiohttp_client.async_get_clientsession(self.hass)
        async with session.post(
            API_URL,
            json={"username": self.username, "password": self.password}
        ) as resp:
            if resp.status != 200:
                raise Exception(f"API error: {resp.status}")
            return await resp.json()
