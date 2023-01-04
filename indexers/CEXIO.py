from decimal import Decimal

import cexio as cexio


class CEXIO:
    def __init__(self, username: str, key: str, secret: str):
        self.username = username
        self.key = key
        self.secret = secret
        self.client = cexio.Api(username, key, secret)

    def get_price(self, ticker: str):
        try:
            return Decimal(self.client.ticker(f'{ticker[:3]}/{ticker[3:]}')['last'])
        except KeyError:
            print(f'{ticker} is not found on CEX.io')

    def get_fees(self, ticker: str = ''):
        return 0.0025