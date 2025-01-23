# src/plugins/market_data_plugin.py
from ..actions import market_data_hookimpl

class MarketDataPlugin:
    @market_data_hookimpl
    def retrieve_market_data(self, symbol):
        return f"Retrieving market data for {symbol}"
