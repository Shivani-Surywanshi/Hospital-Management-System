from django.shortcuts import render, redirect
from reportapp.forms import LabTechRegisterationForm, LabTestForm
from reportapp.models import Lab_Tests, Lab_Tech, all_lab_tests
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib import messages


# REGISTER
def lab_register(request):
    form = LabTechRegisterationForm()

    if request.method == 'POST':
        form = LabTechRegisterationForm(request.POST)

        if form.is_valid():
            user = form.save()

            Lab_Tech.objects.create(
                user=user,
                emp_id=form.cleaned_data['emp_id'],
                qualification=form.cleaned_data['qualification'],
                address=form.cleaned_data['address'],
                year_of_exp=form.cleaned_data['year_of_exp'],
            )

            return redirect('lab_login')

    return render(request, 'reportapp/register.html', {'form': form})


# LOGIN

def lab_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if hasattr(user, 'lab_tech'):
                login(request, user)
                return redirect('lab_home')
            else:
                messages.error(request, "Invalid Lab Technician credentials ❌")
        else:
            messages.error(request, "Invalid username or password ❌")

    return render(request, 'reportapp/login.html')


# HOME
def lab_home(request):
    return render(request, 'reportapp/home.html')


# ALL TESTS

def all_tests(request):

    # Default price & time mapping
    test_data = {
        'CBC': {'price': 200, 'time': '2 Hours'},
        'LFT': {'price': 500, 'time': '6 Hours'},
        'URINE_TOTAL': {'price': 150, 'time': '1 Hour'},
        'URINE_MICRO': {'price': 180, 'time': '1.5 Hours'},
        'SERUM': {'price': 300, 'time': '3 Hours'},
        'THYROID': {'price': 700, 'time': '8 Hours'},
    }

    tests = []

    for code, name in all_lab_tests:
        tests.append({
            'name': name,
            'price': test_data[code]['price'],
            'time': test_data[code]['time']
        })

    return render(request, 'reportapp/all_tests.html', {'tests': tests})


# DASHBOARD (Pagination)
def dashboard(request):
    test_list = Lab_Tests.objects.all().order_by('id')

    paginator = Paginator(test_list, 10)
    page = request.GET.get('page')
    tests = paginator.get_page(page)

    return render(request, 'reportapp/dashboard.html', {
        'tests': tests
    })


# ADD TEST
def add_test(request):
    form = LabTestForm()

    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'reportapp/add_test.html', {'form': form})


# EDIT TEST
def edit_test(request, id):
    test = Lab_Tests.objects.get(id=id)
    form = LabTestForm(instance=test)

    if request.method == 'POST':
        form = LabTestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'reportapp/add_test.html', {'form': form})

