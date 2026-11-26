from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    pass

class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Speciality"
        verbose_name_plural="Specialities"
        
    def __str__(self):
        return self.name

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone = models.CharField(max_length=8)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    # specialites = models.ManyToManyField("AccountApp.Speciality")
    specialites = models.ManyToManyField (Speciality,  related_name="doctors")
    class Meta:
        verbose_name="Doctor"
        verbose_name_plural="Doctors"
    
number_validator = RegexValidator (
    regex=r'^\d{8}$',
    message="National ID must be 8 digits",
)

def validate_birth_date(value):
    if value > timezone.localdate():
        raise ValidationError('La date de naissnace est invalide')

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    class Meta:
            verbose_name="Patient"
            verbose_name_plural="Patients"


