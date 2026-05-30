from django.urls import path
from doctorapp import views

urlpatterns = [
    path('', views.doctor_home, name='doctor_home'),
    path('register/', views.doctor_register, name='doctor_register'),
    path('login/', views.doctor_login, name='doctor_login'),
    path('list/', views.doctor_list, name='doctor_list'),
    path('logout/', views.doctor_logout, name='doctor_logout'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('update/', views.doctor_update, name='doctor_update'),
    path('treatments/', views.treatment_list, name='treatment_list'),
    path('doctors/<int:id>/', views.doctors_by_treatment, name='doctors_by_treatment'),
    path('book/<int:id>/', views.book_appointment, name='book_appointment'),
]