# NextEnergyPricesHA
# NextEnergy Market Prices (Home Assistant Integration)  Fetches and displays NextEnergy market prices for the next 24h.   **Credentials** can be provided via the UI or via `secrets.yaml`:

## Installation

1. Copy the `custom_components/nextenergy` directory to your Home Assistant's `custom_components` folder.
2. Add this repo as a [custom repository in HACS](https://hacs.xyz/docs/faq/custom_repositories/).
3. Restart Home Assistant.
4. Add the integration via the UI and provide your credentials (or use `secrets.yaml`).

## Features

- Fetches prices every day at 16:01 for the next 24h
- Exposes electricity, gas, and trend sensors
- Supports HACS and UI configuration

## License

MIT
