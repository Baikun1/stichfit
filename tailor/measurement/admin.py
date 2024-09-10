from django.contrib import admin
from .models import Measurement

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('measurement_id', 'order', 'user', 'neck', 'chest', 'waist', 'hips')
    search_fields = ('order__order_id', 'user__first_name', 'user__last_name')
