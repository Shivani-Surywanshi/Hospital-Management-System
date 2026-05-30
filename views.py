from django.shortcuts import render, redirect
from doctorapp.forms import AppointmentForm, DoctorForm, DoctorProfileForm, DoctorUpdateForm, DoctorProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from doctorapp.models import DoctorDetails
from django.contrib import messages
from doctorapp.models import Treatment
from django.core.paginator import Paginator



# Doctor Home
def doctor_home(request):
    return render(request, 'doctorapp/doctor_home.html')


# Doctor Registration
def doctor_register(request):
    registered = False

    if request.method == 'POST':
        form1 = DoctorForm(request.POST)
        form2 = DoctorProfileForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            messages.success(request, "Doctor registered successfully ✅")  

        else:
            messages.error(request, "Please correct the errors below ❌")  

    else:
        form1 = DoctorForm()
        form2 = DoctorProfileForm()

    return render(request, 'doctorapp/doctor_register.html', {
        'form1': form1,
        'form2': form2,
        'registered': registered
    })


# ✅ FIXED Doctor Login
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # ✅ Allow only doctors
            if hasattr(user, 'doctordetails'):
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Login successful ✅")
                    return redirect('doctor_dashboard')
                else:
                    messages.error(request, "Account not active ❌")
            else:
                messages.error(request, "Invalid Doctor credentials ❌")
        else:
            messages.error(request, "Invalid username or password ❌")

    return render(request, 'doctorapp/doctor_login.html')


# Doctor List
@login_required(login_url='doctor_login')
def doctor_list(request):
    doctors = DoctorDetails.objects.all()
    return render(request, 'doctorapp/doctor_list.html', {'doctors': doctors})


# Logout
@login_required(login_url='doctor_login')
def doctor_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully 👋")
    return redirect('doctor_login')


# Doctor Dashboard
@login_required(login_url='doctor_login')
def doctor_dashboard(request):
    return render(request, 'doctorapp/doctor_dashboard.html')


# Doctor Profile
@login_required(login_url='doctor_login')
def doctor_profile(request):
    return render(request, 'doctorapp/doctor_profile.html')


@login_required(login_url='doctor_login')
def doctor_update(request):
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=request.user)
        form1 = DoctorProfileUpdateForm(request.POST, request.FILES, instance=request.user.doctordetails)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            from django.contrib import messages
            messages.success(request, "Profile updated successfully ✅")
            return redirect('doctor_profile')
        else:
            from django.contrib import messages
            messages.error(request, "Update failed ❌")

    else:
        form = DoctorUpdateForm(instance=request.user)
        form1 = DoctorProfileUpdateForm(instance=request.user.doctordetails)

    return render(request, 'doctorapp/doctor_update.html', {
        'form': form,
        'form1': form1
    })


def treatment_list(request):
    treatments = Treatment.objects.all()
    return render(request, 'doctorapp/treatment_list.html', {'treatments': treatments})


def doctors_by_treatment(request, id):
    doctors = Treatment.objects.filter(id=id)

    if doctors.exists():
        doctors = doctors
    else:
        doctors = None

    return render(request, 'doctorapp/doctors_by_treatment.html', {'doctors': doctors})


def book_appointment(request, id):
    treatment = Treatment.objects.get(id=id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)   
            appointment.treatment = treatment 
            appointment.user = request.user       
            appointment.save()

            from django.contrib import messages
            messages.success(request, "Appointment Booked Successfully ✅")

            return redirect('treatment_list')

    else:
        form = AppointmentForm()

    return render(request, 'doctorapp/book_appointment.html', {
        'form': form,
        'treatment': treatment
    })



@login_required(login_url='doctor_login')
def doctor_list(request):
    doctor_data = DoctorDetails.objects.all()

    paginator = Paginator(doctor_data, 6)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    return render(request, 'doctorapp/doctor_list.html', {
        'doctors': doctors
    })



@login_required(login_url='login')
def treatment_list(request):
    treatment_data = Treatment.objects.all()

    paginator = Paginator(treatment_data, 6)
    page = request.GET.get('page')
    treatments = paginator.get_page(page)

    return render(request, 'doctorapp/treatment_list.html', {
        'treatments': treatments
    })