from django.db import models
from django.contrib.auth.models import User

class DoctorDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    hospital = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    doctor_pic = models.ImageField(upload_to='doctorimg/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    


class Treatment(models.Model):
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    treatment_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    dos = models.TextField()
    donts = models.TextField()

    def __str__(self):
        return self.treatment_name
    

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    consultation_charge = models.CharField(max_length=100, default="500")

    def __str__(self):
        return f"{self.doctor.user.username} - {self.date}"
    
