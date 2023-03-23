"""Sources: https://www.moneysavingexpert.com/tax-calculator/ inaccuracies when salary > £100,000 for income tax by £2000
https://www.moneysavingexpert.com/banking/tax-rates/ : NI Tax + Income Tax
https://www.gov.uk/repaying-your-student-loan/what-you-pay : Student loan repayment"""


class Taxes:
    def __init__(self, gross_income, council_tax):
        self.gross_income = gross_income
        self.council_tax = council_tax

    def get_income_tax(self):
        personal_allowance = 12570
        """ Calculating personal allowance if it goes over £100,000 
        (goes down by £1 for every £2 earned over)"""
        if self.gross_income > 100000:
            personal_allowance -= (self.gross_income - 100000) / 2
        if personal_allowance < 0:
            personal_allowance = 0

        taxable_income = self.gross_income - personal_allowance
        if taxable_income < 0:
            taxable_income = 0

        # Income Tax
        # First tax band
        if self.gross_income <= 12570:
            income_tax = 0
            # Second tax band
        elif 12571 <= self.gross_income <= 50270:
            income_tax = 0.2 * (self.gross_income - 12570)  # 20% tax
            # Third tax band
        elif 50271 <= self.gross_income <= 150000:
            # I put personal allowance variable here and below because there is a possibility of earning over £100000
            income_tax = 0.4 * (self.gross_income - 50271) + 0.2 * (
                50270 - personal_allowance
            )
            # Fourth tax band
        else:
            income_tax = (
                0.45 * (self.gross_income - 150000)
                + 0.4 * (150000 - 50271)
                + 0.2 * (50270 - personal_allowance)
            )
        return [income_tax, personal_allowance, taxable_income]
        # so income_tax()[0] = income_tax, income_tax[1] = personal_allowance and income_tax[2] = taxable_income

    def get_NI_tax(self):
        # NI Tax
        # First band
        if self.gross_income <= 12570:
            ni_tax = 0
        # Second band
        elif 12571 <= self.gross_income <= 50270:
            ni_tax = 0.1375 * (self.gross_income - 12570)
        # Third band
        else:
            ni_tax = 0.0325 * (self.gross_income - 50271) + 0.1375 * (50270 - 12570)

        return ni_tax

    def get_student_tax(self):
        # Student loan repayment
        if self.gross_income > 27288:  # threshold for loan repayment
            student_tax = (self.gross_income - 27288) * 0.09
        else:
            student_tax = 0
        return student_tax

    def get_total_tax(self):
        return (
            Taxes.get_income_tax(self)[0]
            + Taxes.get_NI_tax(self)
            + self.council_tax
            + Taxes.get_student_tax(self)
        )

    # Total tax without student tax
    def get_total_tax_wost(self):
        return Taxes.get_income_tax(self)[0] + Taxes.get_NI_tax(self) + self.council_tax

    def calculate_income(self):
        return self.gross_income - Taxes.get_total_tax(self)

    def calculate_income_wost(self):
        return self.gross_income - Taxes.get_total_tax_wost(self)


class Budget:
    def __init__(self, rent, bills, food, toiletries, savings, miscellaneous, taxes):
        self.rent = rent
        self.bills = bills
        self.food = food
        self.toiletries = toiletries
        self.savings = savings
        self.miscellaneous = miscellaneous
        self.taxes = taxes

    def calculate_monthly_budget(self):
        return (
            self.rent
            + self.food
            + self.toiletries
            + self.bills
            + self.savings
            + self.miscellaneous
        )

    def calculate_yearly_budget(self):
        return 12 * Budget.calculate_monthly_budget(self)

    def calculate_profit(self):
        return self.taxes.calculate_income() - Budget.calculate_yearly_budget(self)
        # First term utilises a function in the taxes class by including taxes in the initialisation function

    def calculate_profit_wost(self):
        return self.taxes.calculate_income_wost() - Budget.calculate_yearly_budget(self)


def round_twosf(variable):
    return f"{round(variable, 2):,.2f}"


def round_twosf_month(variable):
    return f"{round(variable/12, 2):,.2f}"
