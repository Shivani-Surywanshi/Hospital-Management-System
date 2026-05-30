from django.db import models

ROOM_TYPES = [
    ('Common Ward', 'Common Ward'),
    ('Semi Private', 'Semi Private'),
    ('Private AC', 'Private AC'),
    ('Private Non AC', 'Private Non AC'),
    ('Deluxe', 'Deluxe'),
]

class DischargeSummary(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100)
    description = models.TextField()

    doa = models.DateField()
    dod = models.DateField()

    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    food_required = models.BooleanField(default=False)

    total_days = models.IntegerField()

    def __str__(self):
        return self.patient_name