from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import InvestmentForm
import requests
from datetime import datetime


class InvestmentView(TemplateView):
    template_name='form.html'

    def get(self, request):
        form = InvestmentForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = InvestmentForm(request.POST)
            if form.is_valid():
                investor_amount = form.cleaned_data['investor_amount']
                investment_date = form.cleaned_data['investment_date']
                date_today = datetime.today().strftime('%d-%b-%Y')
                
                print(date_today)
                response = requests.get('http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=53&tp=1&frmdt=01-Apr-2015&todt='+date_today)
                if response.status_code==200:
                    with open('NAV_VALUES.txt', 'w+', encoding="utf-8") as f:
                        f.write(response.text.strip())
                else:
                    pass
                amount = self.calculate_investment(investor_amount, investment_date, date_today)
                context={'form':form,'amount':amount}
                return render(request, self.template_name, context)

    def calculate_investment(self, investor_amount, investment_date, date_today):
        with open('NAV_VALUES.txt','r') as f:
            line = f.readline()
            elements = line.split(';')
            if len(elements)==8 AND elements[1]=='Axis Long Term Equity Fund - Direct Plan - Growth Option':
                if elements[-1]==investment_date:
                    prev_nav_value = elements[-4]
                if elements[-1]==date_today:
                    today_nav_value = elements[]
