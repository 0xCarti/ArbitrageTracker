from decimal import Decimal

import requests
from gemini_api.endpoints.public import Public
from gemini_api.authentication import Authentication


class Gemini:
    def __init__(self, public_key: str = None, private_key: str = None):
        self.base_url = "https://api.gemini.com/v1/"

    def get_price(self, ticker: str):
        request = requests.get(f'{self.base_url}pubticker/{ticker.lower()}')
        return request.json()['last']

    def get_pairs(self):
        pass
