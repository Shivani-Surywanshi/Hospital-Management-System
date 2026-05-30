from django.urls import path
from paymentapp import views

urlpatterns = [
    path('discharge/', views.discharge, name='discharge'),
    path('final_bill/<int:id>/', views.final_bill, name='final_bill'),
]