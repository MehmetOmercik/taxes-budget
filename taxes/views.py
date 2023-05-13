from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import re

from .forms import TaxesForm, BudgetForm
from .functionality.tax_budget_classes import (
    Taxes,
    Budget,
    round_twosf,
    round_twosf_month,
)


# Create your views here.
def Home(request):
    final_results_income = []
    final_results_budget = []
    budget_hide = 1

    # This and the taxes_form below is used to reset or persist data
    taxes_form = TaxesForm()
    budget_form = BudgetForm()
    if "taxes_form" in request.POST:
        taxes_form = TaxesForm(request.POST)
        budget_form = BudgetForm(request.POST)

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
        # Forms process boolean as a string for some reason
        if request.POST["student_loan"] == "True":
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

        final_results_income = [
            [action[0], round_twosf(action[1]), round_twosf_month(action[1])]
            for action in actions_income
        ]

        """ BUDGET SECTION """

        """THIS PART CREATES VARIABLES VIA A FOR LOOP AND LIST"""
        budget_fields = [
            "rent",
            "bills",
            "food",
            "toiletries",
            "savings",
            "miscellaneous",
        ]

        for field in budget_fields:
            globals()[field] = (
                re.sub("[£$,:;_]", "", request.POST[field])
                if request.POST[field] != ""
                else 0
            )

        """This stuff comes up as undefined because these variables arent declared but generated via the loop above"""
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

        rent_f, bills_f, food_f, toiletries_f, savings_f, miscellaneous_f = (
            float(rent),
            float(bills),
            float(food),
            float(toiletries),
            float(savings),
            float(miscellaneous),
        )
        budget = Budget(
            rent_f,
            bills_f,
            food_f,
            toiletries_f,
            savings_f,
            miscellaneous_f,
            gross_income,
        )

        actions_budget = [["Yearly Budget", budget.calculate_yearly_budget()]]

        if request.POST["student_loan"] == "True":
            actions_budget.append(["Profit/Loss", budget.calculate_profit()])
        else:
            actions_budget.append(["Profit/Loss", budget.calculate_profit_wost()])

        final_results_budget = [
            [
                action[0],
                f"£{round_twosf(action[1])}",
                f"£{round_twosf_month(action[1])}",
            ]
            for action in actions_budget
        ]

        if final_results_budget[0][1] != "£0.00":
            budget_hide = 0

    context = {
        "TaxesForm": taxes_form,
        "BudgetForm": budget_form,
        "final_results_income": final_results_income,
        "final_results_budget": final_results_budget,
        "budget_hide": budget_hide,
    }
    return render(request, "taxes.html", context)
