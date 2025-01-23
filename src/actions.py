# src/actions.py
import pluggy

pricing_hookimpl = pluggy.HookimplMarker("derivatives_pricing")
market_data_hookimpl = pluggy.HookimplMarker("market_data_retrieval")

class DerivativesPricingPluginSpec:
    @pluggy.HookspecMarker("derivatives_pricing")
    def price_derivative(self, derivative):
        pass

class MarketDataPluginSpec:
    @pluggy.HookspecMarker("market_data_retrieval")
    def retrieve_market_data(self, symbol):
        pass
