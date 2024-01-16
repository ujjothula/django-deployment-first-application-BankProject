from django import forms;
from bankapp.models import Bank

class BankForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
    class Meta:
        model=Bank
        fields='__all__'