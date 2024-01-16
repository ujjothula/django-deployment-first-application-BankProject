from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from bankapp.forms import BankForm
from bankapp.models import Bank
# Create your views here.
def index_view(request):
    return render(request,'bankapp/index.html')

def add_Bank_view(request):
    formObj=BankForm()
    if request.method=="POST":
        formObj=BankForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['Bankdate'])
            print(formObj.cleaned_data['Bankname'])
            print(formObj.cleaned_data['firstname'])
            print(formObj.cleaned_data['lastname'])
            print(formObj.cleaned_data['AccountNumber'])
            print(formObj.cleaned_data['IFSCcode'])
            print(formObj.cleaned_data['Email'])

            formObj.save()	#auto-commit
            return index_view(request)
    return render(request, 'bankapp/addBank.html',{'form1':formObj})

def list_Bank_view(request):
    Bank_list=Bank.objects.all().order_by('lastname') #(-)desc-order
    return render(request,'bankapp/listbank.html',{'movies_list':Bank_list})