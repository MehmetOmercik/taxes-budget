from django.shortcuts import render, redirect
from django.contrib import messages
import re

from .forms import TaxesForm
from .Tax_And_Budget_Classes import Taxes, Budget, round_twosf, round_twosf_month

# Create your views here.
def Home(request):
    context = {"TaxesForm": TaxesForm()}
    if "taxes_form" in request.POST:
        print(request.POST)

        # Remove unneccesary characters
        gross_salary = re.sub("[£$,:;_]", "", request.POST["gross_salary"])
        council_tax = re.sub("[£$,:;_]", "", request.POST["council_tax"])

        # Checking for anything other than int or float
        try:
            float(gross_salary) and float(council_tax)
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
        actions = [
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
            actions.append(["Student Loan", gross_income.get_student_tax()])
            actions.append(["Total Deductions", gross_income.get_total_tax()])
            actions.append(["Total Income", gross_income.calculate_income()])
        else:
            actions.append(["Total Deductions", gross_income.get_total_tax_wost()])
            actions.append(["Total Income", gross_income.calculate_income_wost()])

        final_results = []

        for action in actions:
            final_results.append(
                [
                    action[0],
                    f"£{round_twosf(action[1])}",
                    f"£{round_twosf_month(action[1])}",
                ]
            )

        context = {"TaxesForm": TaxesForm(), "final_results": final_results}

    return render(request, "taxes.html", context)
