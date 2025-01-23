# src/plugins/pricing_plugin.py
from ..actions import pricing_hookimpl

class PricingPlugin:
    @pricing_hookimpl
    def price_derivative(self, derivative):
        return f"Pricing the {derivative} derivative"
