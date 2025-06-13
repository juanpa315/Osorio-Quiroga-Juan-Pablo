from django.urls import path
from . import views 

urlpatterns =[
    path("index/", views.index, name="index"),
    path("employee/", views.employee, name="employee"),
    path("customer/", views.customer, name="customer"),
    path("coe/", views.coe, name="coe"),
    path("job/", views.job, name="job"),
    path("insert/", views.insert, name="insert"),
    path("update/<int:record_id>", views.update_form, name="update_form"),
    path("update/", views.update, name="update"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]