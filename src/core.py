# src/core.py
import pluggy
from .plugins.pricing_plugin import PricingPlugin
from .plugins.market_data_plugin import MarketDataPlugin
from .actions import DerivativesPricingPluginSpec, MarketDataPluginSpec

class DerivativesPlatform:
    def __init__(self):
        self.pm = pluggy.PluginManager("derivatives_pricing")
        self.pm.add_hookspecs(DerivativesPricingPluginSpec)

        self.market_data_pm = pluggy.PluginManager("market_data_retrieval")
        self.market_data_pm.add_hookspecs(MarketDataPluginSpec)

        self._register_plugins()

    def _register_plugins(self):
        self.pm.register(PricingPlugin())
        self.market_data_pm.register(MarketDataPlugin())

    def execute_action(self, action_name, *args, **kwargs):
        if action_name == "price_derivative":
            hooked = self.pm.hook.__getattr__(action_name)(*args, **kwargs)
        elif action_name == "retrieve_market_data":
            hooked = self.market_data_pm.hook.__getattr__(action_name)(*args, **kwargs)
        else:
            raise ValueError(f"Unknown action: {action_name}")
        return hooked
