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

    def test_get_NI_tax(self):
        ni = self.test_taxes.get_NI_tax()
        assert ni == 2396.625

    def test_get_student_tax(self):
        st = self.test_taxes.get_student_tax()
        assert round(st, 2) == 244.08

    def test_get_total_tax(self):
        tt = self.test_taxes.get_total_tax()
        assert round(tt, 2) == 7126.70

    def test_get_total_tax_wost(self):
        tt_wost = self.test_taxes.get_total_tax_wost()
        assert round(tt_wost, 2) == 6882.62

    def test_calculate_income(self):
        ci = self.test_taxes.calculate_income()
        assert ci == 22_873.295

    def test_calculate_income_wost(self):
        ci_wost = self.test_taxes.calculate_income_wost()
        assert ci_wost == 23117.375
