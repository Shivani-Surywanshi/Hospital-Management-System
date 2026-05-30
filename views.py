from django.shortcuts import render, redirect
from userapp.forms import UserForm, UserProfileForm, UserProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib import messages   
from doctorapp.models import Appointment
from django.core.paginator import Paginator
from doctorapp.models import Appointment
from django.contrib.auth.decorators import login_required


# Registration
def registeration(request):
    registered = False

    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
           
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            messages.success(request, "User registered successfully ✅")

        else:
            messages.error(request, "Please correct the errors ❌")

    else:
        form1 = UserForm()
        form2 = UserProfileForm()

    return render(request, "userapp/registeration.html", {
        'form1': form1,
        'form2': form2,
        'registered': registered
    })


# ✅ FIXED USER LOGIN (IMPORTANT 🔥)
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # ❌ Block doctors here
            if hasattr(user, 'doctordetails'):
                messages.error(request, "Please login from Doctor portal ❌")
                return redirect('login')

            if user.is_active:
                login(request, user)
                messages.success(request, "Login successful ✅")
                return redirect("home")
            else:
                messages.error(request, "User is not active ❌")
        else:
            messages.error(request, "Invalid username or password ❌")

    return render(request, "userapp/login.html")


# Home
@login_required(login_url="login")
def home(request):
    return render(request, "userapp/home.html")


# Profile
@login_required(login_url="login")
def profile(request):
    return render(request, "userapp/profile.html")


# Logout
@login_required(login_url="login")
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully 👋")
    return redirect("login")


# Update Profile
@login_required(login_url="login")
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        form1 = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userdetails)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            messages.success(request, "Profile updated successfully ✅")
            return redirect('profile')
        else:
            messages.error(request, "Update failed ❌")

    else:
        form = UserUpdateForm(instance=request.user)
        form1 = UserProfileUpdateForm(instance=request.user.userdetails)

    return render(request, "userapp/update.html", {
        'form': form,
        'form1': form1
    })



@login_required(login_url="login")
def profile(request):
    appointments = Appointment.objects.filter(user=request.user)

    return render(request, "userapp/profile.html", {
        'appointments': appointments
    })



@login_required(login_url="login")
def profile(request):

    appointment_list = Appointment.objects.filter(
        user=request.user
    ).order_by('id')

    paginator = Paginator(appointment_list, 3)
    page = request.GET.get('page')
    appointments = paginator.get_page(page)

    return render(request, "userapp/profile.html", {
        'appointments': appointments
    })













    