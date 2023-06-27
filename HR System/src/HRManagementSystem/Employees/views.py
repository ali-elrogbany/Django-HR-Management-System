from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import CreateForm
from .forms import UpdateForm

from .models import Employee

# Create your views here.
def Create_view(request):
    context = {}

    form = CreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/employees")
    
    context['form']= form
    return render(request, "EmployeeCreate.html", context)

def Read_view(request):
    context = {}

    context["data"] = Employee.objects.all()

    return render(request, 'EmployeeRead.html', context)

def Update_view(request, id):
    context = {}

    obj = get_object_or_404(Employee, id = id)

    form = UpdateForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect("/employees")
    
    context['form']= form
    return render(request, "EmployeeUpdate.html", context)

def Delete_view(request, id):
    context = {}

    obj = get_object_or_404(Employee, id = id)

    obj.delete()
    return HttpResponseRedirect("/Employee")