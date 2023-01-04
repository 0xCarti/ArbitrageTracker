class MarketManager:
    def __init__(self):
        self.enabled_markets = {}
        self.all_markets = {
            'ETHUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'ETHEUR': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'ETHCAD': [
                'kraken',
            ],
            'BTCUSD': [
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'BTCEUR': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'BTCCAD': [
                'kraken',
            ],
            'LTCUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'LTCEUR': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
            ],
            'LTCCAD': [
                # 'kraken',
            ],
            'XRPUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'XRPEUR': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
            ],
            'XRPCAD': [
                'kraken',
            ],
            'SOLUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'SOLEUR': [
                'binance',
                'kraken',
                # 'gemini',
            ],
            'MATICUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'MATICEUR': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
            ],
            'MATICCAD': [
                'kraken',
            ],
            'DOTUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'cexio',
                'bitfinex',
            ],
            'DOTEUR': [
                'binance',
                'kraken',
                # 'gemini',
            ],
            'XMRUSD': [
                'binance',
                'kraken',
                # 'gemini',
                'bitfinex',
            ],
            'XMREUR': [
                'kraken',
                # 'gemini',
            ],}

    def enable_markets(self, *markets: str):
        for market in markets:
            if market in self.all_markets:
                self.enabled_markets[market] = self.all_markets[market]

    def disable_markets(self, *markets: str):
        for market in markets:
            if market in self.enabled_markets:
                self.enabled_markets.pop(market)

    def get(self, market: str):
        if market in self.enabled_markets:
            return self.enabled_markets[market]
        else:
            return self.all_markets[market]

    def __iter__(self):
        return self.enabled_markets.__iter__()