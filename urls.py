from django.urls import path
from userapp import views

urlpatterns=[
    path('',views.registeration,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.user_logout,name='logout'),
    path('update',views.update,name='update'),
]