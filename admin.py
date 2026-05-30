from django.contrib import admin
from doctorapp.models import Treatment
from doctorapp.models import Appointment

# Register your models here.

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['treatment_name', 'doctor']

admin.site.register(Treatment, TreatmentAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'treatment', 'date', 'time_slot', 'consultation_charge']

    search_fields = ['user__username']
    list_filter = ['date']

admin.site.register(Appointment, AppointmentAdmin)
