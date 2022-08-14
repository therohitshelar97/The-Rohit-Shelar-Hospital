from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['Patient_Name', 'Patient_Age', 'Date_Of_Appointment', 'Time_Of_Appointment']
