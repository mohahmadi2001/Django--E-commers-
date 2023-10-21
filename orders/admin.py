from django.contrib import admin
from .models import Order,OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_field = ('product',)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','update','paid')
    list_filter = ('paid',)
    inlines = (OrderItemAdmin,)
    
    