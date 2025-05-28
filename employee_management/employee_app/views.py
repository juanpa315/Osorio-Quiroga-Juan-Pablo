from django.shortcuts import render

def employee(request):
    return render(request, "employee_app/employee.html")

def baseform(request):
    return render(request, "employee_app/baseform.html")