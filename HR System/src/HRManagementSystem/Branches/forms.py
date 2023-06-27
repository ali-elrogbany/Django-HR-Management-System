from django import forms
from django.contrib import admin 

from .models import Branch
from Employees.models import Employee

class CreateForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'buildingNumber', 'street', 'area', 'city', 'country']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'buildingNumber', 'street', 'area', 'city', 'country', 'manager']

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['manager'].queryset = Employee.objects.filter(currentBranch=self.instance)

class SupplierAdmin(admin.ModelAdmin):
    form = UpdateForm