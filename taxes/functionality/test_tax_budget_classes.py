import pytest
from .tax_budget_classes import Taxes, Budget, round_twosf, round_twosf_month


class Test_Taxes:
    test_taxes = Taxes(gross_income=30_000, council_tax=1000)

    def test_instantiation(self):
        gi, ct = self.test_taxes.get_instantiation()
        assert gi == 30_000
        assert ct == 1000

    def test_get_income_tax(self):
        income_tax, personal_income, taxable_income = self.test_taxes.get_income_tax()
        assert income_tax == 3486.00
        assert personal_income == 12_570.00
        assert taxable_income == 17_430.00
