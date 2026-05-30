from django import forms
from paymentapp.models import DischargeSummary
from doctorapp.models import DoctorDetails, Treatment
from reportapp.models import Lab_Tests


class DischargeSummaryForm(forms.ModelForm):

    patient_name = forms.ModelChoiceField(
        queryset=Lab_Tests.objects.all(),
        empty_label="Select Patient",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    doctor_name = forms.ModelChoiceField(
        queryset=DoctorDetails.objects.all(),
        empty_label="Select Doctor",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    treatment = forms.ModelChoiceField(
        queryset=Treatment.objects.all(),
        empty_label="Select Treatment",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    class Meta:
        model = DischargeSummary
        fields = '__all__'

        widgets = {

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter treatment / discharge summary'
            }),

            'doa': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'doa'
            }),

            'dod': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'dod'
            }),

            'room_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'food_required': forms.Select(
                choices=[(True, 'Yes'), (False, 'No')],
                attrs={'class': 'form-select'}
            ),

            'total_days': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'total_days',
                'readonly': True,
                'placeholder': 'Auto Calculated'
            }),
        }