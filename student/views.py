from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('stName')
        roll = request.POST.get('stRoll')
        address = request.POST.get('stAddress')
        studentData = Student(name=name, roll=roll, address=address)
        studentData.save()
    return render(request, 'student/create.html')


def showall(request):
    return render(request, 'student/showall.html')


def update(request):
    return render(request, 'student/update.html')


def delete(request):
    return render(request, 'student/delete.html')
