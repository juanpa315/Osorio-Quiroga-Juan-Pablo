from django.shortcuts import render

def index(request):
    
    return render(request, "employee_app/index.html")