from django import forms

CHOICES = [(False, "No"), (True, "Yes")]


class TaxesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    gross_salary = forms.CharField(
        label="What is your annual Gross Salary? £", max_length=10
    )
    council_tax = forms.CharField(
        label="What is your annual Council tax? £", max_length=10
    )
    student_loan = forms.TypedChoiceField(
        label="Are you repaying student loan?", choices=CHOICES
    )


class BudgetForm(forms.Form):
    rent = forms.CharField(
        label="What is your monthly rent? £", max_length=10, required=False
    )
    bills = forms.CharField(
        label="What is your monthly bills? £", max_length=10, required=False
    )
    food = forms.CharField(
        label="What is your monthly food budget? £", max_length=10, required=False
    )
    toiletries = forms.CharField(
        label="What is your monthly toiletries budget? £", max_length=10, required=False
    )
    savings = forms.CharField(
        label="What is your monthly savings? £", max_length=10, required=False
    )
    miscellaneous = forms.CharField(
        label="What is your monthly miscellaneous budget? £",
        max_length=10,
        required=False,
    )
