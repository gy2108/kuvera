from django import forms
import datetime
# from django.core.exceptions import ValidationError

class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(help_text="Enter the Amount to invest", required=True)
    investment_date = forms.DateField(initial=datetime.date.today, 
        widget=forms.widgets.DateInput(format = '%d-%b-%Y'),help_text="Enter a Date In Format(01 Jan 2019)",
        input_formats=('%d-%b-%Y',), required=True) 
