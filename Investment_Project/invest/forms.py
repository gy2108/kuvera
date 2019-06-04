from django import forms
import datetime
# from django.core.exceptions import ValidationError

class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(help_text="Enter the Amount to invest", required=True)
    investment_date = forms.DateField(initial=datetime.date.today, help_text="Enter a Date", required=True) 
