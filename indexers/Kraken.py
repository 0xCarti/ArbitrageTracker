import time
from decimal import Decimal

from krakipy import KrakenAPI, CallRateLimitError


class Kraken:
    def __init__(self):
        self.client = KrakenAPI()

    def get_price(self, ticker: str):
        try:
            return Decimal(self.client.get_ticker_information(ticker).iloc[0].get('c')[0])
        except ConnectionError as e:
            print(e)
        except CallRateLimitError:
            time.sleep(5)
            return self.get_price(ticker)

    def get_pairs(self):
        return self.client.get_tradable_asset_pairs()['altname'].values
