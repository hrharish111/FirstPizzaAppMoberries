from django.contrib import admin
from .models import Order,OrderItems
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order

class ItemAdmin(admin.ModelAdmin):
    model = OrderItems

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItems,ItemAdmin)
