from django.contrib import admin
from django.contrib import admin
from bankapp.models import Bank
from django import forms;
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display=['Bankdate','Bankname','firstname', 'lastname','AccountNumber','IFSCcode','Email'];

admin.site.register(Bank,BankAdmin);