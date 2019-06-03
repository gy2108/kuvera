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

class CalcView(TemplateView):
    def get(self, request):
        print("============")
        if request.method == 'GET':
            form = InvestmentForm(request.GET)
            if form.is_valid():
                investor_amount = form.cleaned_data['investor_amount']
                investment_date = form.cleaned_date['investment_date']

                context={'amt':investor_amount,'date':investment_date}
                return render(request, self.template_name, context)
