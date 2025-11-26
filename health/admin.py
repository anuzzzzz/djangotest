from django.contrib import admin
from .models import Prescription, Event

# Register your models here.

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient_name','medication_name','status','updated_at']
    list_filter = ['status']
    search_fields = ['patient_name', 'medication_name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['prescription','event_type','performed_by','created_at']
    list_filter = ['event_type']

