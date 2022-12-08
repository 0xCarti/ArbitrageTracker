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
            'kraken': Kraken(),
            'gemini': Gemini(),
            'cexio': CEXIO(),
            'bitfinex': Bitfinex()
        }

    def get_indexer(self, name: str):
        return self.indexers[name]