from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import InvestmentForm

# def investmentView(request, template_name='form.html'):
#     return render(request, template_name)

class InvestmentView(TemplateView):
    template_name='form.html'

    def get(self, request):
        form = InvestmentForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            form = InvestmentForm(request.POST)
            if form.is_valid():
                investor_amount = form.cleaned_data['investor_amount']
                investment_date = form.cleaned_data['investment_date']

                context={'form':form,'amount':investor_amount}
                return render(request, self.template_name, context)
