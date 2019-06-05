from django import forms
import datetime
# from django.core.exceptions import ValidationError

class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(help_text="Enter the Amount to invest", required=True)
    investment_date = forms.DateField(initial=datetime.date.today,
                        help_text="Enter a Date In 'YYYY-MM-DD' format after '2016-04-01'",required=True) 
