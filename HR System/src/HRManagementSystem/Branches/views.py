from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import CreateForm
from .forms import UpdateForm

from .models import Branch
from Employees.models import Employee

# Create your views here.
def Create_view(request):
    context = {}

    form = CreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/branches")
    
    context['form']= form
    return render(request, "BranchCreate.html", context)

def Read_view(request):
    context = {}

    context["data"] = Branch.objects.all()

    return render(request, 'BranchRead.html', context)

def Update_view(request, id):
    context = {}

    obj = get_object_or_404(Branch, id = id)

    form = UpdateForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect("/branches")
    
    context['form']= form
    return render(request, "BranchUpdate.html", context)

def Delete_view(request, id):
    context = {}

    obj = get_object_or_404(Branch, id = id)

    obj.delete()
    return HttpResponseRedirect("branches/")

def BranchEmployees_view(request, id):
    context = {}

    context["branch"] = get_object_or_404(Branch, id = id)

    context["data"] = Employee.objects.filter(currentBranch = id)

    return render(request, "BranchEmployee.html", context)