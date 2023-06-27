from django import forms

from .models import Employee

class CreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'email', 'phone', 'currentBranch']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'email', 'phone', 'currentBranch']