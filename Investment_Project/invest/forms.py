from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from .models import InvestItem

class InvestmentForm(forms.Form):
    investor_amount = forms.IntegerField(required=True)
    investment_date = forms.DateField(help_text="Enter a Date", required=True) 

    def clean_investment_date(self):
        data = self.cleaned_data['investment_date']
        if data>datetime.date.today():
            raise ValidationError(_("Invalid Date"))
        
        return data

    def clean_investor_amount(self):
        data = self.cleaned_data['investor_amount']
        if data is not int:
            raise ValidationError(_("Invalid Amount"))
        return data