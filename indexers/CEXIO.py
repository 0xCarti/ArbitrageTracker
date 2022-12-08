from decimal import Decimal

import cexio as cexio


class CEXIO:
    def __init__(self, username: str, key: str, secret: str):
        self.username = username
        self.key = key
        self.secret = secret
        self.client = cexio.Api(username, key, secret)

    def get_price(self, ticker: str):
        return Decimal(self.client.ticker(f'{ticker[:3]}/{ticker[3:]}')['last'])

    def get_pairs(self):
        pass