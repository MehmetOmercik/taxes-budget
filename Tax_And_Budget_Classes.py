"""Sources: https://www.moneysavingexpert.com/tax-calculator/ inaccuracies when salary > £100,000 for income tax by £2000
https://www.moneysavingexpert.com/banking/tax-rates/ : NI Tax + Income Tax
https://www.gov.uk/repaying-your-student-loan/what-you-pay : Student loan repayment"""


class Taxes:
    def __init__(self, gross_income, council_tax):
        self.gross_income = gross_income
        self.council_tax = council_tax

    def incomeTax(self):
        personalAllowance = 12570
        """ Calculating personal allowance if it goes over £100,000 
        (goes down by £1 for every £2 earned over)"""
        if self.gross_income > 100000:
            personalAllowance -= (self.gross_income - 100000) / 2
        if personalAllowance < 0: personalAllowance = 0

        taxableIncome = self.gross_income - personalAllowance
        if taxableIncome < 0: taxableIncome = 0

        # Income Tax
        # First tax band
        if self.gross_income <= 12570:
            incomeTax = 0
            # Second tax band
        elif 12571 <= self.gross_income <= 50270:
            incomeTax = 0.2 * (self.gross_income - 12570)  # 20% tax
            # Third tax band
        elif 50271 <= self.gross_income <= 150000:
            # I put personal allowance variable here and below because there is a possibility of earning over £100000
            incomeTax = 0.4 * (self.gross_income - 50271) + 0.2 * \
                        (50270 - personalAllowance)
            # Fourth tax band
        else:
            incomeTax = 0.45 * (self.gross_income - 150000) + 0.4 * \
                        (150000 - 50271) + 0.2 * (50270 - personalAllowance)
        return [incomeTax, personalAllowance, taxableIncome]
        # so incomeTax()[0] = incomeTax, incomeTax[1] = personalAllowance and incomeTax[2] = taxableIncome

    def NItax(self):
        # NI Tax
        # First band
        if self.gross_income <= 12570:
            NItax = 0
        # Second band
        elif 12571 <= self.gross_income <= 50270:
            NItax = 0.1375 * (self.gross_income - 12570)
        # Third band
        else:
            NItax = 0.0325 * (self.gross_income - 50271) + 0.1375 * (50270 - 12570)

        return NItax

    def studentTax(self):
        # Student loan repayment
        if self.gross_income > 27288:  # threshold for loan repayment
            studentTax = (self.gross_income - 27288) * 0.09
        else:
            studentTax = 0
        return studentTax

    def totalTaxWS(self):
        return Taxes.incomeTax(self)[0] + Taxes.NItax(self) + self.council_tax + Taxes.studentTax(self)

    def totalTaxWOS(self):
        return Taxes.incomeTax(self)[0] + Taxes.NItax(self) + self.council_tax

    def calculateIncomeWS(self):
        return self.gross_income - Taxes.totalTaxWS(self)

    def calculateIncomeWOS(self):
        return self.gross_income - Taxes.totalTaxWOS(self)


class Budget:
    def __init__(self, rent, bills, food, toiletries,
                 savings, miscellaneous, taxes):
        self.rent = rent
        self.bills = bills
        self.food = food
        self.toiletries = toiletries
        self.savings = savings
        self.miscellaneous = miscellaneous
        self.taxes = taxes

    def calculateMonthlyBudget(self):
        return self.rent + self.food + self.toiletries + self.bills + self.savings + self.miscellaneous

    def calculateYearlyBudget(self):
        return 12 * Budget.calculateMonthlyBudget(self)

    def calculateProfitWS(self):
        return self.taxes.calculateIncomeWS() - Budget.calculateYearlyBudget(self)
        # First term utilises a function in the taxes class by including taxes in the initialisation function

    def calculateProfitWOS(self):
        return self.taxes.calculateIncomeWOS() - Budget.calculateYearlyBudget(self)
