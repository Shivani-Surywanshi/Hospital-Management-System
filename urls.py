from django.urls import path
from reportapp import views

urlpatterns = [
    path('register/', views.lab_register, name='lab_register'),
    path('login/', views.lab_login, name='lab_login'),
    path('home/', views.lab_home, name='lab_home'),
    path('tests/', views.all_tests, name='all_tests'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_test, name='add_test'),
    path('edit/<int:id>/', views.edit_test, name='edit_test'),
]