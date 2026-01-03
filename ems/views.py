from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee, Department

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_department(request):
    if request.method == 'POST':
        Department.objects.create(name=request.POST['name'])
        return redirect('dashboard')
    return render(request, 'add_department.html')

@login_required
def add_employee(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            salary=request.POST['salary'],
            join_date=request.POST['join_date'],
            department_id=request.POST['department']
        )
        return redirect('employee_list')
    return render(request, 'add_employee.html', {'departments': departments})

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})