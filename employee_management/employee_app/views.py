from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'employee_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, "employee_app/index.html")

@login_required
def employee(request):
    db_data = Employees.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }

    return render(request, "employee_app/employee.html", context)

@login_required
def customer(request):
    db_data = Customers.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }

    return render(request, "employee_app/customer.html", context)

@login_required
def coe(request):
    db_data = Coe.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }

    return render(request, "employee_app/coe.html", context)

@login_required
def job(request):
    db_data = JobPositions.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    return render(request, "employee_app/job_position.html", context)

@login_required
def insert(request):
    form_id = request.POST.get("form_id") 
    page = ""
    if form_id == "employeeForm":
        try:
            employee_record = {
                'cedula': request.POST.get("cedula", ""),
                'first_name': request.POST.get("first_name", ""),
                'last_name': request.POST.get("last_name", ""),
                'age': request.POST.get("age", ""),
                'gender': request.POST.get("gender", ""),
                'salary': request.POST.get("salary", ""),
                'date_of_entry': request.POST.get("date_of_entry", ""),
                'withdrawal_date': request.POST.get("withdrawal_date", ""),
                'position_id': request.POST.get("position", ""),
                'assigned_customers_id': request.POST.get("assigned_customers", ""),
                'seniority_id': request.POST.get("seniority", ""),
                'coe_id': request.POST.get("coe", "")
            }
            db_data= Employees(**employee_record)
            db_data.save()
            page="employee"
        except ValueError as e:
            print(e) 
    elif form_id == "customerForm":
        try:
            customer_record = {
                'customer_name': request.POST.get("customer_name", ""),
                'start_date': request.POST.get("start_date", ""),
                'end_date': request.POST.get("end_date", ""),
                'contract_type_id': request.POST.get("contract_type", "")
            }
            db_data= Customers(**customer_record)
            db_data.save()
            page="customer"
        except ValueError as e:
            print(e)
    elif form_id == "coeForm":
        try:
            coe = {
                'name': request.POST.get("name", ""),
                'description': request.POST.get("description", ""),
            }
            db_data= Coe(**coe)
            db_data.save()
            page="coe"
        except ValueError as e:
            print(e)  
    elif form_id == "jobForm":
        try:
            job_position = {
                'position_name': request.POST.get("position_name", ""),
                'junior_salary': request.POST.get("junior_salary", ""),
                'middle_salary': request.POST.get("middle_salary", ""),
                'senior_salary': request.POST.get("senior_salary", ""),
                'coe_id': request.POST.get("coe", "") or None,
            }
            db_data = JobPositions(**job_position)
            db_data.save()
            page = "job"
        except ValueError as e:
            print(e)
    
    return HttpResponseRedirect(reverse(page))

@login_required
def update_form(request, record_id):
    form_id = request.GET.get("form_id")
    print("form is: ", form_id)
    page = ""
    context = {}
    if form_id == "employeeForm":
        page = "employee_app/employee.html"
        db_data = Employees.objects.all()
        db_data_only = Employees.objects.get(pk=record_id)
        context = {
            "db_data": db_data[::-1],
            "update": db_data_only
        }
    elif form_id == "customerForm":
        db_data = Customers.objects.all()
        db_data_only = Customers.objects.get(pk=record_id)
        context = {
            "db_data": db_data[::-1],
            "update": db_data_only
        }
        page = "employee_app/customer.html"  
    elif form_id == "coeForm":
        db_data = Coe.objects.all()
        db_data_only = Coe.objects.get(pk=record_id)
        context = {
            "db_data": db_data[::-1],
            "update": db_data_only
        }
        page = "employee_app/coe.html"
    elif form_id == "jobForm":
        db_data = JobPositions.objects.all()
        db_data_only = JobPositions.objects.get(pk=record_id)
        context = {
            "db_data": db_data[::-1],
            "update": db_data_only
        }
        page = "employee_app/job_position.html"

    return render(request, page, context)

@login_required
def update(request):
    form_id = request.POST.get("form_id") 
    page = ""
    if form_id == "employeeForm":
        employee = {
                'id_employee': request.POST.get("id_employee", ""),
                'cedula': request.POST.get("cedula", ""),
                'first_name': request.POST.get("first_name", ""),
                'last_name': request.POST.get("last_name", ""),
                'age': request.POST.get("age", ""),
                'gender': request.POST.get("gender", ""),
                'salary': request.POST.get("salary", ""),
                'date_of_entry': request.POST.get("date_of_entry", ""),
                'withdrawal_date': request.POST.get("withdrawal_date", ""),
                'position_id': request.POST.get("position", ""),
                'assigned_customers_id': request.POST.get("assigned_customers", ""),
                'seniority_id': request.POST.get("seniority", ""),
                'coe_id': request.POST.get("coe", "")
        }
        employee_id = request.POST["id_employee"]
        Employees.objects.filter(pk=employee_id).update(**employee)
        page="employee"
    elif form_id == "customerForm":
        customer = {
                'customer_name': request.POST.get("customer_name", ""),
                'start_date': request.POST.get("start_date", ""),
                'end_date': request.POST.get("end_date", ""),
                'contract_type_id': request.POST.get("contract_type", "")
            }
        record_id = request.POST["customer_id"]
        Customers.objects.filter(pk=record_id).update(**customer)
        page="customer"
    elif form_id == "coeForm":
        coe = {
                'name': request.POST.get("name", ""),
                'description': request.POST.get("description", ""),
            }
        record_id = request.POST["coe_id"]
        Coe.objects.filter(pk=record_id).update(**coe)
        page="coe"
    elif form_id == "jobForm":
        job_position = {
            'position_name': request.POST.get("position_name", ""),
            'junior_salary': request.POST.get("junior_salary", ""),
            'middle_salary': request.POST.get("middle_salary", ""),
            'senior_salary': request.POST.get("senior_salary", ""),
            'coe_id': request.POST.get("coe", "") or None,
        }
        record_id = request.POST["position_id"] 
        JobPositions.objects.filter(pk=record_id).update(**job_position)
        page = "job"
    return HttpResponseRedirect(reverse(page)) 
