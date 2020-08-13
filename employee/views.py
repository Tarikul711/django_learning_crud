from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def home(request):
    employeeData = Employee
    context = {
        "employee": employeeData
    }
    return render(request, 'index.html', context)


def profile(request):
    return render(request, 'employee/profile.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
