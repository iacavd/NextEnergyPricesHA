# NextEnergy Market Prices (Home Assistant Integration)

Fetches and displays NextEnergy market prices for the next 24h, supporting both Market and Market+ rates.

## Credentials

Provide via UI or in `secrets.yaml`:

```
nextenergy_username: "YOUR_USERNAME"
nextenergy_password: "YOUR_PASSWORD"
```

## Installation

1. Add this repo as a [custom repository in HACS](https://hacs.xyz/docs/faq/custom_repositories/).
2. Install via HACS.
3. Restart Home Assistant.
4. Add the integration via the UI and provide your credentials (or use `secrets.yaml`).

## Sensors

- `sensor.nextenergy_current_market`
- `sensor.nextenergy_current_market_plus`
- `sensor.nextenergy_next_market`
- `sensor.nextenergy_next_market_plus`

## Notes

- Market = raw exchange price.
- Market+ = all-in price (market + taxes + VAT).

## License

MIT
