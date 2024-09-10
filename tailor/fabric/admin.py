from django.contrib import admin
from .models import Fabric, Design

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ('fabric_id', 'name', 'price_per_meter')
    search_fields = ('name',)

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('design_id', 'order', 'user', 'design_name', 'design_date')
    search_fields = ('design_name', 'user__first_name', 'user__last_name')
