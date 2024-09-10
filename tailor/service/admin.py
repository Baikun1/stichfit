from django.contrib import admin
from .models import Service, Consultant, Consultation

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'base_price', 'estimated_time')
    search_fields = ('service_name',)

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')
    search_fields = ('name', 'specialty')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('consultation_id', 'user', 'consultant', 'consultation_date')
    list_filter = ('consultation_date',)
