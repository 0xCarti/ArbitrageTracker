from decimal import Decimal

import cexio as cexio


class CEXIO:
    def __init__(self):
        self.client = cexio.Api('up157490572', 'KL5mrR281Eaxzrj0nW7zduxGCag', 'OO4xlVFJSBV6GyYTMNeQWqRs')

    def get_price(self, ticker: str):
        return Decimal(self.client.ticker(f'{ticker[:3]}/{ticker[3:]}')['last'])

    def get_pairs(self):
        pass