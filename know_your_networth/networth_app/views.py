from django.shortcuts import render
from .forms import NetWorthForm

def home(request):
    if request.method == 'POST':
        form = NetWorthForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            net_worth = (data['liquid_money'] + data['stocks_value'] +
                         data['mutual_funds'] + data['us_stocks'] +
                         data['crypto'] + data['debt_funds'] - data['liabilities'])
            return render(request, 'networth_app/result.html', {'net_worth': net_worth})
    else:
        form = NetWorthForm()
    return render(request, 'networth_app/home.html', {'form': form})