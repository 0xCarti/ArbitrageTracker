from decimal import Decimal
from bitfinex import Client
from bitfinex.rest.restv1 import BitfinexException
from requests import ReadTimeout


class Bitfinex:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.client = Client()

    def get_price(self, ticker: str):
        try:
            return Decimal(self.client.ticker(ticker)['last_price'])
        except ReadTimeout as e:
            print(e)
        except BitfinexException as e:
            print(f'{e} - {ticker}')

    def get_pairs(self):
        pass

    def get_fees(self, ticker: str = ''):
        return 0.2