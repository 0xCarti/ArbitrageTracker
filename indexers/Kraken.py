import requests


class Kraken:
    def __init__(self):
        self.base_url = 'https://api.kraken.com/0/public/'

    def get_price(self, ticker: str):
        ticker = f'X{ticker[:3]}Z{ticker[3:]}'
        if 'BTC' in ticker:
            ticker = ticker.replace('BTC', 'XBT')
        request = requests.get(f'{self.base_url}Ticker?pair={ticker}')
        return request.json()['result'][ticker]['c'][0]


    def get_pairs(self):
        pass

