from decimal import Decimal
from binance import Client
from binance.exceptions import BinanceAPIException


class Binance:
    def __init__(self, key: str, secret: str):
        self.API_KEY = key
        self.API_SECRET = secret
        self.client = Client(self.API_KEY, self.API_SECRET)

    def get_price(self, ticker: str):
        if 'USD' in ticker:
            ticker = ticker.replace('USD', 'USDT')
        try:
            return Decimal(self.client.get_ticker(symbol=ticker)['lastPrice'])
        except BinanceAPIException:
            print(f'{ticker} is not found on Binance.')

    def get_pairs(self):
        return self.client.get_all_tickers()

    def get_fees(self, ticker: str = ''):
        if 'USD' in ticker:
            ticker = ticker.replace('USD', 'USDT')
        data = self.client.get_trade_fee(symbol=ticker)
        return Decimal(data[0]['takerCommission'])
