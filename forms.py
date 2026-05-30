from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from reportapp.models import Lab_Tech, Lab_Tests



class LabTechRegisterationForm(UserCreationForm):
    emp_id = forms.IntegerField()
    qualification = forms.CharField(max_length=29)
    address = forms.CharField(max_length=200)
    year_of_exp = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LabTestForm(forms.ModelForm):
    class Meta:
        model = Lab_Tests
        fields = '__all__'