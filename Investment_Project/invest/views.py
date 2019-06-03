from django.shortcuts import render
import datetime

class InvestItem(models.Model):
    date = models.DateField(_("Date"))
    amount = models.IntegerField()