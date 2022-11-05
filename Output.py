import Tax_And_Budget_Classes as tb

# gross_income = int(input("Please enter your annual gross salary: "))

gi = 20000
ct = 2000
gross_income = tb.Taxes(gi, ct)
print(f"Annual Gross Income: £{gi:.2f} (£{(gi)/12:.2f} per month)"
    f"\n Tax-Free Allowance: £{round(gross_income.incomeTax()[1],2):.2f} (£{round((gross_income.incomeTax()[1])/12,2):.2f} per month) "
    f"\n     Taxable Income: £{round(gross_income.incomeTax()[2],2):.2f} (£{round((gross_income.incomeTax()[2])/12,2):.2f} per month) "
      
  f"\n\n         Income Tax: £{round(gross_income.incomeTax()[0], 2):.2f}  (£{round((gross_income.incomeTax()[0])/12, 2):.2f} per month)"
    f"\n             NI Tax: £{round(gross_income.NItax(), 2):.2f} (£{round((gross_income.NItax())/12, 2):.2f} per month)"
    f"\n        Student Tax: £{round(gross_income.studentTax(), 2):.2f} (£{round((gross_income.studentTax())/12, 2):.2f} per month) "
    f"\n        Council Tax: £{ct:.2f} (£{ct/12:.2f} per month)"
  f"\n\n     Overall Income: £{round(gross_income.calculateIncomeWS(), 2):.2f} (£{round((gross_income.calculateIncomeWS())/12, 2):.2f} per month with student tax)"
    f"\n     Overall Income: £{round(gross_income.calculateIncomeWOS(), 2):.2f} (£{round((gross_income.calculateIncomeWOS())/12, 2):.2f} per month without student tax)")

budget = tb.Budget(1000, 200, 100, 20, 100, 10, gross_income) #rent, bills, food, toiletries, savings, miscellaneous
print(f"\n      Yearly Budget: £{round(budget.calculateYearlyBudget(),2):.2f} (£{round(budget.calculateMonthlyBudget(),2):.2f} per month)"
     f"\n\n        Profit/Loss: £{round(budget.calculateProfitWS(), 2):.2f} (£{round((budget.calculateProfitWS()) / 12, 2):.2f} per month with student tax)"
    f"\n        Profit/Loss: £{round(budget.calculateProfitWOS(), 2):.2f} (£{round((budget.calculateProfitWOS()) / 12, 2):.2f} per month without student tax)")

