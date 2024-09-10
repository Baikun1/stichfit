from django.contrib import admin
from .models import User, Admin, Session

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'registration_date', 'last_login')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'user', 'created_at', 'expires_at')
    list_filter = ('created_at',)
