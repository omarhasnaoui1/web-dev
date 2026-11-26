from django.db import models
from AccountApp.models import Doctor
from AccountApp.models import Patient
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(blank=True, upload_to='prescriptions/')
    class Status(models.TextField):
        PENDING = "PENDING",  "En attente"
        CONFIRMED = "CONFIRMED",  "Confirmé"
        CANCELLED = "CANCELLED",  "Annulé"
    status = models.CharField(
        max_length=10,
        choices=[
            ("PENDING", "En attente"),
            ("CONFIRMED", "Confirmé"),
            ("CANCELLED", "Annulé")
        ],
        default="PENDING"
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)    
    # Patient = models.ForeignKey("AccountApp.Patient", on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    
    def clean(self):
        modified_date=self._state.adding or {
            Appointment.objects.filter(
                pk=self.pk,appointment_date=self.appointment_date
            ).exists()
        }
        if modified_date and self.appointment_date <= timezone.now():
            raise ValidationError("la date du rdv doit être supérieur à la date d'aujourd'hui")
        
    class Meta:
        ordering=["-appointment_date"]
        constraints=[
            models.UniqueConstraint(
                fields=["doctor", "appointment_date"],
                name="unicite_patient_doctor_date",
                violation_error_code="Ce docteur possède un rendez-vous avec cette date"
            )
        ]
        
    def __str__(self):
        return f"Le rdv est pour la raison {self.reason}"