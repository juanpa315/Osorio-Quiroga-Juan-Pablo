from django.urls import path
from . import views 

urlpatterns =[
    path("employee/", views.employee, name="employee"),
    path("baseform/", views.baseform, name="baseform")
]