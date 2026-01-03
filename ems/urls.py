from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-department/', views.add_department, name='add_department'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employees/', views.employee_list, name='employee_list'),
    path('logout/', views.logout_view, name='logout'),
]