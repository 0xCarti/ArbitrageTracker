from decimal import Decimal
from binance import Client


class Binance:
    def __init__(self, key: str, secret: str):
        self.API_KEY = key
        self.API_SECRET = secret
        self.client = Client(self.API_KEY, self.API_SECRET)

    def get_price(self, ticker: str):
        if 'USD' in ticker:
            ticker = ticker.replace('USD', 'USDT')
        return Decimal(self.client.get_ticker(symbol=ticker)['lastPrice'])

    def get_pairs(self):
        return self.client.get_all_tickers()
