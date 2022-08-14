from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Patient_Name = models.CharField(max_length=70)
    Patient_Age = models.IntegerField()
    Date_Of_Appointment = models.DateField()
    Time_Of_Appointment = models.TimeField()
    
