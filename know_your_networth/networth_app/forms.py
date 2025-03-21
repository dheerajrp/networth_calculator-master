from django import forms
from .models import NetWorth

class NetWorthForm(forms.ModelForm):
    class Meta:
        model = NetWorth
        fields = '__all__'