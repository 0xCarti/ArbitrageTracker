import time
from decimal import Decimal

from krakipy import KrakenAPI, CallRateLimitError, KrakenAPIError


class Kraken:
    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret
        self.client = KrakenAPI(key, secret)

    def get_price(self, ticker: str):
        try:
            return Decimal(self.client.get_ticker_information(ticker).iloc[0].get('c')[0])
        except ConnectionError as e:
            print(e)
        except CallRateLimitError:
            time.sleep(5)
            return self.get_price(ticker)
        except KrakenAPIError as e:
            print(f'{ticker} is not found on Kraken.')

    def get_pairs(self):
        return self.client.get_tradable_asset_pairs()['altname'].values

    def get_fees(self, ticker: str = ''):
        #return Decimal(self.client.get_trade_volume(ticker)[2]['fee'][0])
        return 0.2
