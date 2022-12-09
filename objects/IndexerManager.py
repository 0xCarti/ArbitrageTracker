import os
from dotenv import load_dotenv
from indexers.Binance import Binance
from indexers.Bitfinex import Bitfinex
from indexers.CEXIO import CEXIO
from indexers.Kraken import Kraken
from indexers.Gemini import Gemini


class IndexerManager:
    def __init__(self):
        load_dotenv()
        self.indexers = {
            'binance': Binance(os.getenv('BINANCE_KEY'), os.getenv('BINANCE_SECRET')),
            'kraken': Kraken(os.getenv('KRAKIPY_KEY'), os.getenv('KRAKIPY_SECRET')),
            'gemini': Gemini(),
            'cexio': CEXIO(os.getenv('CEXIO_USERNAME'), os.getenv('CEXIO_KEY'), os.getenv('CEXIO_SECRET')),
            'bitfinex': Bitfinex(os.getenv('BITFINEX_KEY'), os.getenv('BITFINEX_SECRET'))
        }

    def get_indexer(self, name: str):
        return self.indexers[name]