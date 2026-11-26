from django.contrib import admin
from .models import Appointment
# Register your models here.
#admin.site.register(Appointement)

@admin.action(description="make them confirmed")
def confirmed_appointment(model,req, queryset):
    queryset.update(status="CONFIRMED")

@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    actions=[confirmed_appointment]
    list_display=("reason", "status", "duration_minutes", "appointment_date")
    list_filter=("status", "appointment_date")
    list_editable=("status",)
    search_fields=("reason", "status")
    ordering=("appointment_date",)
    fieldsets=(
        ('Description',{
            "fields":("reason", "status", "prescription")
        }),
        ('Date',{
            "fields":("appointment_date", "duration_minutes")
        }),
        ('Patients/Doctors',{
            "fields":("doctor", "patient")
        }),
        ('Planification',{
            "fields":("created_at", "updated_at")
        })
    )
    readonly_fields=("created_at", "updated_at")    
#class AppointmentAdminPers(admin.ModelAdmin):
#    list_display=("reason", "status", "duration_minutes", "appointment_date")
#    list_filter=("status", "appointment_date")
#    list_editable=("status",)
#admin.site.register(Appointement,AppointmentAdminPers)