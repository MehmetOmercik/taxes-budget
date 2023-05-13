import pytest
from .tax_budget_classes import Taxes, Budget, round_twosf, round_twosf_month


@pytest.mark.parametrize(
    "test_input, expected", [(34_001.455, "£34,001.46"), (3000, "£3,000.00")]
)
def test_round_twosf(test_input, expected):
    assert round_twosf(test_input) == expected


def test_round_twosf_month():
    number = 34_001.455
    assert round_twosf_month(number) == "£2,833.45"


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


class Test_Budget:
    test_budget = Budget(
        rent=1000,
        bills=500,
        food=100,
        toiletries=30,
        savings=100,
        miscellaneous=100,
        taxes=Test_Taxes.test_taxes,
    )

    def test_instantiation(self):
        assert self.test_budget.rent == 1000
        assert self.test_budget.bills == 500
        assert self.test_budget.food == 100
        assert self.test_budget.toiletries == 30
        assert self.test_budget.savings == 100
        assert self.test_budget.miscellaneous == 100
        assert self.test_budget.taxes == Test_Taxes.test_taxes

    def test_calculate_monthly_budget(self):
        mb = self.test_budget.calculate_monthly_budget()
        assert mb == 1830

    def test_calculate_yearly_budget(self):
        yb = self.test_budget.calculate_yearly_budget()
        assert yb == 21_960

    def test_calculate_profit(self):
        profit = self.test_budget.calculate_profit()
        assert round(profit, 2) == 913.29

    def test_calculate_profit_wost(self):
        profit = self.test_budget.calculate_profit_wost()
        assert round(profit, 2) == 1157.38
