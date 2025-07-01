from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class NextEnergyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Try credentials
            return self.async_create_entry(title="NextEnergy", data=user_input)

        # Try to fetch from secrets.yaml
        secrets = self.hass.data.get("secrets", {})
        username = secrets.get("nextenergy_username", "")
        password = secrets.get("nextenergy_password", "")

        data_schema = vol.Schema({
            vol.Required("username", default=username): str,
            vol.Required("password", default=password): str,
        })
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
