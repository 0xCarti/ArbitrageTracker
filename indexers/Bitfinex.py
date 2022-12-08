from bitfinex import Client
from decimal import Decimal

from requests import ReadTimeout


class Bitfinex:
    def __init__(self):
        self.client = Client()

    def get_price(self, ticker: str):
        try:
            return Decimal(self.client.ticker(ticker.lower())['last_price'])
        except ReadTimeout as e:
            print(e)

    def get_pairs(self):
        pass