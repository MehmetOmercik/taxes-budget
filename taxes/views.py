from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import re

from .forms import TaxesForm, BudgetForm
from .Tax_And_Budget_Classes import Taxes, Budget, round_twosf, round_twosf_month

# Create your views here.
def Home(request):
    final_results_income = []
    final_results_budget = []
    budget_hide = 1
    if "taxes_form" in request.POST:
        # print(request.POST)

        """INCOME SECTION"""

        # Remove unneccesary characters
        gross_salary = re.sub("[£$,:;_]", "", request.POST["gross_salary"])
        council_tax = re.sub("[£$,:;_]", "", request.POST["council_tax"])

        # Checking for anything other than int or float
        try:
            float(gross_salary) or float(council_tax)
        except:
            messages.error(
                request,
                "Incorrect input for either gross salary or council tax, please try again",
            )
            return redirect("home")

        gi = float(gross_salary)
        ct = float(council_tax)
        gross_income = Taxes(gi, ct)

        # All calculations that need to be done
        actions_income = [
            ["Gross Income", gi],
            ["Tax-Free Allowance", gross_income.get_income_tax()[1]],
            ["Taxable Income", gross_income.get_income_tax()[2]],
            ["Income Tax", gross_income.get_income_tax()[0]],
            ["NI Tax", gross_income.get_NI_tax()],
            ["Council Tax", ct],
        ]

        # Checking whether the user selected the student loan or not and appends functions to actions
        if request.POST["student_loan"] == "True":
            # Forms process boolean as a string for some reason
            actions_income.append(["Student Loan", gross_income.get_student_tax()])
            actions_income.append(["Total Deductions", gross_income.get_total_tax()])
            actions_income.append(["Total Income", gross_income.calculate_income()])
        else:
            actions_income.append(
                ["Total Deductions", gross_income.get_total_tax_wost()]
            )
            actions_income.append(
                ["Total Income", gross_income.calculate_income_wost()]
            )

        for action in actions_income:
            final_results_income.append(
                [
                    action[0],
                    f"£{round_twosf(action[1])}",
                    f"£{round_twosf_month(action[1])}",
                ]
            )

        """ BUDGET SECTION """
        rent = (
            re.sub("[£$,:;_]", "", request.POST["rent"])
            if request.POST["rent"] != ""
            else 0
        )
        bills = (
            re.sub("[£$,:;_]", "", request.POST["bills"])
            if request.POST["bills"] != ""
            else 0
        )

        food = (
            re.sub("[£$,:;_]", "", request.POST["food"])
            if request.POST["food"] != ""
            else 0
        )

        toiletries = (
            re.sub("[£$,:;_]", "", request.POST["toiletries"])
            if request.POST["toiletries"] != ""
            else 0
        )

        savings = (
            re.sub("[£$,:;_]", "", request.POST["savings"])
            if request.POST["savings"] != ""
            else 0
        )

        miscellaneous = (
            re.sub("[£$,:;_]", "", request.POST["miscellaneous"])
            if request.POST["miscellaneous"] != ""
            else 0
        )

        # Checking for anything other than int or float
        try:
            float(rent) or float(bills) or float(food) or float(toiletries) or float(
                savings
            ) or float(miscellaneous)
        except:
            messages.error(
                request,
                "Incorrect input within budget section",
            )
            return redirect("home")
        rent, bills, food, toiletries, savings, miscellaneous = (
            float(rent),
            float(bills),
            float(food),
            float(toiletries),
            float(savings),
            float(miscellaneous),
        )
        budget = Budget(
            rent, bills, food, toiletries, savings, miscellaneous, gross_income
        )

        actions_budget = [["Yearly Budget", budget.calculate_yearly_budget()]]

        if request.POST["student_loan"] == "True":
            actions_budget.append(["Profit/Loss", budget.calculate_profit()])
        else:
            actions_budget.append(["Profit/Loss", budget.calculate_profit_wost()])

        for action in actions_budget:
            final_results_budget.append(
                [
                    action[0],
                    f"£{round_twosf(action[1])}",
                    f"£{round_twosf_month(action[1])}",
                ]
            )

        if final_results_budget[0][1] != "£0.00":
            budget_hide = 0

    context = {
        "TaxesForm": TaxesForm(),
        "BudgetForm": BudgetForm(),
        "final_results_income": final_results_income,
        "final_results_budget": final_results_budget,
        "budget_hide": budget_hide,
    }
    return render(request, "taxes.html", context)
