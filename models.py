from django.db import models
from django.contrib.auth.models import User
from doctorapp.models import DoctorDetails
from userapp.models import UserDetails


all_lab_tests = [
    ('CBC', 'CBC'),
    ('LFT', 'LFT'),
    ('URINE_TOTAL', 'Urine total test'),
    ('URINE_MICRO', 'Urine microscopic'),
    ('SERUM', 'Serum routine'),
    ('THYROID', 'Thyroid'),
]

test_range = [
    ('NIL', 'Nil'),
    ('POSITIVE', 'Positive'),
    ('NEGATIVE', 'Negative'),
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
]


class Lab_Tech(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.IntegerField()
    qualification = models.CharField(max_length=20)
    year_of_exp = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Lab_Tests(models.Model):
    reffered_by = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    # patient_name = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    lab_test = models.CharField(max_length=100, choices=all_lab_tests)
    lab_result = models.CharField(max_length=20, default='ONGOING')
    created_at = models.DateTimeField(auto_now_add=True)
    result_range = models.CharField(max_length=20, choices=test_range, default='NIL')
    result_desc = models.TextField()
    test_cost = models.IntegerField()

    def __str__(self):
        return str(self.patient_name)