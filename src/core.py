import pluggy
from .plugins.pricing_plugin import PricingPlugin
from .plugins.market_data_plugin import MarketDataPlugin
from .actions import DerivativesPricingPluginSpec, MarketDataPluginSpec

class DerivativesPlatform:
    def __init__(self):
        self.pm = pluggy.PluginManager("derivatives_pricing")
        self.pm.add_hookspecs(DerivativesPricingPluginSpec)
        self.pm.add_hookspecs(MarketDataPluginSpec)

        self._register_plugins()

    def _register_plugins(self):
        self.pm.register(PricingPlugin())
        self.pm.register(MarketDataPlugin())
