from django import forms
from django.contrib.auth.models import User
from doctorapp.models import DoctorDetails, Appointment
from django_recaptcha.fields import ReCaptchaField


class DoctorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DoctorProfileForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = DoctorDetails
        fields = ['specialization', 'experience', 'hospital', 'phone', 'doctor_pic']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class DoctorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = DoctorDetails
        fields = ['specialization', 'experience', 'hospital', 'phone', 'doctor_pic']


class AppointmentForm(forms.ModelForm):
    consultation_charge = forms.CharField(
        initial="500",
        disabled=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    TIME_SLOTS = [
        ('10:00-12:00', '10:00-12:00'),
        ('12:00-14:00', '12:00-14:00'),
        ('15:00-17:00', '15:00-17:00'),
    ]

    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time_slot', 'consultation_charge']

        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'form-control'
            }),

            'date': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
        }