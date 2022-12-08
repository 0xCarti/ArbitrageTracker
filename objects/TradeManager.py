from __future__ import annotations
from forex_python.converter import CurrencyRates
from objects.IndexerManager import IndexerManager
from objects.Settings import Settings
from objects.ThreadManager import ThreadManager


class PairException(Exception):
    def __init__(self, message):
        super().__init__(message)


class TradeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Pair:
    def __init__(self, exchange: str, ticker: str, price: float = 0.0):
        self.exchange = exchange
        self.ticker = ticker
        self.asset_one = ticker[:3]
        self.asset_two = ticker[3:]

    def reverse(self):
        copy_asset = self.asset_one
        self.asset_one = self.asset_two
        self.asset_two = copy_asset

    def copy(self):
        return Pair(self.exchange, self.ticker)

    def __repr__(self):
        return f'{self.exchange} - {self.asset_one}/{self.asset_two}'


class Trade:
    def __init__(self, buy_pair: Pair, sell_pair: Pair):
        self.buy_pair = buy_pair
        self.sell_pair = sell_pair
        self.initial_currency = self.buy_pair.asset_two
        self.ending_currency = self.sell_pair.asset_two
        self.profit = 0.0

    def update_profit(self, indexer_manager: IndexerManager, rate_converter: CurrencyRates):
        buy_indexer = indexer_manager.get_indexer(self.buy_pair.exchange)
        buy_curr = self.buy_pair.asset_two
        buy_price = buy_indexer.get_price(self.buy_pair.ticker)
        sell_indexer = indexer_manager.get_indexer(self.sell_pair.exchange)
        sell_curr = self.sell_pair.asset_two
        sell_price = sell_indexer.get_price(self.sell_pair.ticker)
        if buy_curr != sell_curr:
            sell_price = rate_converter.convert(sell_curr, buy_curr, sell_price)
        self.profit = sell_price - buy_price
        return self.profit

    def reverse(self):
        return Trade(self.sell_pair, self.buy_pair)

    def code(self) -> str:
        return f'{self.buy_pair.exchange}{self.buy_pair.ticker}{self.sell_pair.exchange}{self.sell_pair.ticker}'

    def __repr__(self):
        buy_trade = f'[{self.buy_pair.exchange}, {self.buy_pair.ticker}]'.center(20, ' ')
        sell_trade = f'[{self.sell_pair.exchange}, {self.sell_pair.ticker}]'.center(20, ' ')
        return f"{buy_trade} ---> {sell_trade}"


class TradeManager:
    def __init__(self, indexer_manager: IndexerManager, settings: Settings, threads: ThreadManager):
        self.indexer_manager = indexer_manager
        self.settings = settings
        self.threads = threads
        self.rate_converter = CurrencyRates()
        self.trades = {}
        pass

    def create_trade(self, buy_exchange: str, buy_asset: str, sell_exchange: str, sell_asset: str):
        if buy_exchange == sell_exchange and buy_asset == sell_asset:
            raise TradeException(f'Trade Failed - Same Pair')
        buy_pair = Pair(buy_exchange, buy_asset)
        sell_pair = Pair(sell_exchange, sell_asset)
        if buy_pair.asset_one == sell_pair.asset_one:
            trade = Trade(buy_pair, sell_pair)
            reverse_code = trade.reverse().code()
            if reverse_code not in self.trades:
                self.trades[trade.code()] = trade
                return trade
        raise TradeException(f'Trade Failed - {buy_pair.asset_one}/{sell_pair.asset_one}')

    def monitor(self, start_index: int, end_index: int, thread_name: str):
        trade_codes = list(self.trades.keys())[start_index:end_index]
        for trade_code in trade_codes:
            trade, reverse_trade = self.trades[trade_code], self.trades[trade_code].reverse()
            profit = trade.update_profit(self.indexer_manager, self.rate_converter)
            reverse_profit = reverse_trade.update_profit(self.indexer_manager, self.rate_converter)
            if profit > self.settings.get('price_thresh'):
                while True:
                    if not self.settings.lock:
                        self.settings.lock = True
                        print(f'{trade}\t[${profit:.6f} {trade.buy_pair.asset_two}]')
                        self.settings.lock = False
                        break
            elif reverse_profit > self.settings.get('price_thresh'):
                while True:
                    if not self.settings.lock:
                        self.settings.lock = True
                        print(f'{reverse_trade}\t[${reverse_profit:.6f} {reverse_trade.buy_pair.asset_two}]')
                        self.settings.lock = False
                        break
        self.threads.stop_thread(thread_name)

    def reverse_trade(self):
        pass



