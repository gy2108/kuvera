from django import forms
import datetime
from django.contrib.admin.widgets import AdminDateWidget


class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(label="Investment Amount", min_value=1, required=True)
    investment_date = forms.DateField(widget=forms.SelectDateWidget(), label="Investment Date",
                        help_text="Enter a Date after 1st April 2016 and on or Before 6th Jun 2019",required=True) 
