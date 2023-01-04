This a simple console bot I made in Python to track various arbitrage trading opportunities across various cryptocurrency exchanges. The bot can monitor any market as long as the market is available on one of the included exchange indexers. This bot is still in the early stages of development and may lack some features, please feel free to leave contact me with any suggestions to add to it.

## Supported Exchanges:
- Binance
- Kraken
- CEX.io
- Bitfinex
- ~~Gemini~~ _**BROKEN**_

### TO-DO - v1
- Add transaction fee variable to profit output **(currently static fees, needs to use api to update)**
- Implement simulated trade functionality
- Track 30d trading volume
- Enhance settings and add saving/loading functionality.
- Fix the Gemini Module.
- ~~Add a requirements.txt for all the python packages~~
- Implement command line args

### TO-DO - v2
- Implement notification module

#

##### Note: You must create a .env file with values for:
- BINANCE_KEY=
- BINANCE_SECRET=
- BITFINEX_KEY=
- BITFINEX_SECRET=
- CEXIO_USERNAME=
- CEXIO_KEY=
- CEXIO_SECRET=
- KRAKIPY_KEY=
- KRAKIPY_SECRET=

Discord: Carti#8173