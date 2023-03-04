from django.shortcuts import render
from django.contrib import messages
import re

from .forms import TaxesForm
from .Tax_And_Budget_Classes import Taxes, Budget

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
            return render(request, "taxes.html", context)

        gs = float(gross_salary)
        ct = float(council_tax)

    return render(request, "taxes.html", context)
