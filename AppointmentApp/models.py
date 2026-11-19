from django.db import models
from AccountApp.models import Doctor
from AccountApp.models import Patient
# Create your models here.
class Appointement(models.Model):
    reason = models.TextField()
    prescription = models.FileField(blank=True, upload_to='prescriptions/')
    class Status(models.Model):
        PENDING = "PENDING",  "En attente"
        CONFIRMED = "CONFIRMED",  "Confirmé"
        CANCELLED = "CANCELLED",  "Annulé"
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField()
    Doctor = models.ForeignKey(Doctor)
    # Patient = models.ForeignKey("AccountApp.Patient", on_delete=models.CASCADE, related_name="appointments")
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")