from django import forms
import datetime
from django.contrib.admin.widgets import AdminDateWidget


class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(help_text="Enter the Amount to invest", min_value=1, required=True)
    investment_date = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today,
                        help_text="Enter a Date In 'YYYY-MM-DD' format after '2016-04-01'",required=True) 
