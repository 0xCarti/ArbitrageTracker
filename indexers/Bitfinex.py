import requests

class Bitfinex:
    def __init__(self):
        self.base_url = 'https://api-pub.bitfinex.com/v2/ticker/'

    def get_price(self, ticker: str):
        request = requests.get(f'{self.base_url}t{ticker}')
        return request.json()[6]

    def get_pairs(self):
        pass

