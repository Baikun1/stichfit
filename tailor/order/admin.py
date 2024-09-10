from django.contrib import admin
from .models import Order, OrderTracking, Payment, ReviewRating

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'service', 'order_date', 'total_price', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('user__first_name', 'user__last_name', 'service__service_name')

@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'order', 'status', 'update_time')
    list_filter = ('status', 'update_time')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'user', 'amount', 'payment_date', 'payment_method')
    list_filter = ('payment_method', 'payment_date')

@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'order', 'user', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
