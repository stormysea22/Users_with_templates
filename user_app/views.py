from django.shortcuts import render, redirect
from .models import Employee

def index(request):
    context = {
        "employees" : Employee.objects.all()
        }      
    return render(request, "index.html", context)

def new_employee(request):
    return render(request, "new_employee.html")

def create_employee(request):
    Employee.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )
    return redirect('/')