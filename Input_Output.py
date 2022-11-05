import Tax_And_Budget_Classes as tb
import time

# import os

# Taxes inputs
print("This program is used to calculate your taxes depending on gross income and your budget if you want")
time.sleep(5)
gi = float(input("\nPlease enter your annual gross salary: £"))  # Gross Income
ct = float(input("Please enter your annual council tax: £"))  # Council Tax

gross_income = tb.Taxes(gi, ct)

# Option1 = student loan selection, option2 = budget selection. Also while loops to ensure they input the correct results
option1 = input("Are you repaying student loan? Please write Y/N (Yes or No) to decide: ")
while option1 != "Y" and option1 != "y" and option1 != "N" and option1 != "n":
    option1 = input("Im sorry I did not understand that, please input Y or N to continue: ")

option2 = input("Would you like to include a budget? Please write Y/N (Yes or No) to decide: ")
while option2 != "Y" and option2 != "y" and option2 != "N" and option2 != "n":
    option2 = input("Im sorry I did not understand that, please input Y or N to continue: ")

# If they have selected yes for budget then print these inputs
if option2 == "y" or option2 == "Y":
    rent = int(input("\nPlease enter your monthly rent: £"))  # Rent
    bills = int(input("Please enter your monthly bills: £"))  # Bills
    food = int(input("Please enter your monthly food budget: £"))  # Food
    toiletries = int(input("Please enter your monthly toiletries budget: £"))  # Toiletries
    savings = int(input("Please enter your monthly savings: £"))  # Savings
    miscellaneous = int(input("Please enter your monthly miscellaneous budget: £"))  # Miscellaneous
    budget = tb.Budget(rent, bills, food, toiletries, savings, miscellaneous,
                       gross_income)  # rent, bills, food, toiletries, savings, miscellaneous

# print("\n"*100)
# os.system('cls')
print("\nLoading, please wait...")
time.sleep(3)

# Income section results. These results print no matter the initial conditionals (options 1 and 2)
print("\nIncome and Tax\n----------------------------------------------------------")
print(f"Annual Gross Income: £{gi:.2f} (£{(gi) / 12:.2f} per month)"
      f"\n Tax-Free Allowance: £{round(gross_income.incomeTax()[1], 2):.2f} (£{round((gross_income.incomeTax()[1]) / 12, 2):.2f} per month) "
      f"\n     Taxable Income: £{round(gross_income.incomeTax()[2], 2):.2f} (£{round((gross_income.incomeTax()[2]) / 12, 2):.2f} per month) "

      f"\n\n         Income Tax: £{round(gross_income.incomeTax()[0], 2):.2f}  (£{round((gross_income.incomeTax()[0]) / 12, 2):.2f} per month)"
      f"\n             NI Tax: £{round(gross_income.NItax(), 2):.2f} (£{round((gross_income.NItax()) / 12, 2):.2f} per month)"
      f"\n        Council Tax: £{ct:.2f} (£{ct / 12:.2f} per month)")

# Conditional sections. This prints the statements whether they have said yes or no to student loan or budget
if option1 == "Y" or option1 == "y":  # Student loan
    print(
        f"        Student Tax: £{round(gross_income.studentTax(), 2):.2f} (£{round((gross_income.studentTax()) / 12, 2):.2f} per month) "
        f"\n        Overall Tax: £{round(gross_income.totalTaxWS(), 2):.2f} (£{round((gross_income.totalTaxWS()) / 12, 2):.2f} per month with student tax) "
        f"\n    Overall Income: £{round(gross_income.calculateIncomeWS(), 2):.2f} (£{round((gross_income.calculateIncomeWS()) / 12, 2):.2f} per month with student tax)")
    if option2 == "Y" or option2 == "y":  # Student loan + budget
        print("\nBudget\n----------------------------------------------------------"
              f"\n      Yearly Budget: £{round(budget.calculateYearlyBudget(), 2):.2f} (£{round(budget.calculateMonthlyBudget(), 2):.2f} per month)"
              f"\n        Profit/Loss: £{round(budget.calculateProfitWS(), 2):.2f} (£{round((budget.calculateProfitWS()) / 12, 2):.2f} per month with student tax)")


else:  # No student loan
    print(
        f"        Overall Tax: £{round(gross_income.totalTaxWOS(), 2):.2f} (£{round((gross_income.totalTaxWOS()) / 12, 2):.2f} per month without student tax) "
        f"\n     Overall Income: £{round(gross_income.calculateIncomeWOS(), 2):.2f} (£{round((gross_income.calculateIncomeWOS()) / 12, 2):.2f} per month without student tax)")
    if option2 == "Y" or option2 == "y":  # No student loan + budget
        print(f"\nBudget\n----------------------------------------------------------"
              f"\n      Yearly Budget: £{round(budget.calculateYearlyBudget(), 2):.2f} (£{round(budget.calculateMonthlyBudget(), 2):.2f} per month) "
              f"\n        Profit/Loss: £{round(budget.calculateProfitWOS(), 2):.2f} (£{round((budget.calculateProfitWOS()) / 12, 2):.2f} per month without student tax)")
