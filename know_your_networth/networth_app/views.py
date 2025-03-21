from django.shortcuts import render
from .forms import NetWorthForm

def home(request):
    if request.method == 'POST':
        form = NetWorthForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            net_worth = (
                data['liquid_money'] + data['fds'] + data['stocks_value'] + data['mutual_funds'] + data['us_stocks'] +
                data['crypto'] + data['debt_funds'] + data['epf'] + data['ppf'] + data['vpf'] + data['nps'] +
                data['sukanya_samruddhi_yojna'] + data['senior_citizen_savings_scheme'] + data['jewellery'] + data['sgb'] + 
                data['gold_etf'] + data['digital_gold'] + data['silver'] + data['home_value'] + data['land_value'] + data['reits']
            )
            return render(request, 'networth_app/result.html', {'net_worth': net_worth})
    else:
        form = NetWorthForm()
    return render(request, 'networth_app/home.html', {'form': form})