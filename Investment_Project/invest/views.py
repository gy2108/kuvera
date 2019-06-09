from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import InvestmentForm
import requests
from datetime import datetime

# MONTH_DICT = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May',
#                 '06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}

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
                # date_split = investment_date.split('-')
                # investment_date = date_split[-1]+'-'+MONTH_DICT[date_split[1]]+'-'+date_split[0]
                investment_date = investment_date.strftime('%d-%b-%Y')
                date_today = datetime.today().strftime('%d-%b-%Y')
                date_today='31-May-2019'
                response = requests.get('http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=53&tp=1&frmdt=01-Apr-2015&todt='+date_today)
                if response.status_code==200:
                    with open('NAV_VALUES.txt', 'w+', encoding="utf-8") as f:
                        f.write(response.text.strip())
                amount = self.calculate_investment(investor_amount, investment_date, date_today)
                context={'form':form,'amount':amount}   
                return render(request, self.template_name, context)
            else:
                context = {'form':form}
                return render(request, self.template_name, context)


    def calculate_investment(self, investor_amount, investment_date, date_today):
        flag = False
        prev_nav_value=1.0
        today_nav_value=1.0
        with open('NAV_VALUES.txt','r') as f:
            for line in f:
                elements = line.strip().split(';')
                if len(elements)==8 and elements[1]=='Axis Long Term Equity Fund - Direct Plan - Growth Option':
                    if elements[-1]==investment_date:
                        prev_nav_value = float(elements[-4])
                        flag = True
                    if elements[-1]==date_today:
                        today_nav_value = float(elements[-4])
                        if flag==True:
                            break
        amount = (investor_amount/prev_nav_value)*today_nav_value
        return round(amount, 2)
