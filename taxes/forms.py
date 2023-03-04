from django import forms

CHOICES = [(False, "No"), (True, "Yes")]


class TaxesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    gross_salary = forms.CharField(
        label="What is your annual Gross Salary? £", max_length=50
    )
    council_tax = forms.CharField(
        label="What is your annual council tax? £", max_length=50
    )
    student_loan = forms.TypedChoiceField(
        label="Are you repaying student loan?", choices=CHOICES
    )
    budget = forms.TypedChoiceField(
        label="Would you like to include a budget?", choices=CHOICES
    )
