from django.contrib import admin
from .models import Pizza,PizzaSize,PizzaVariation

# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    """admin can view pizza"""
    model = Pizza

class PizzaSizeAdmin(admin.ModelAdmin):
    """admin can see pizza size"""
    model = PizzaSize

class PizzaVarityAdmin(admin.ModelAdmin):
    """admin can see pizza varity"""
    model = PizzaVariation


admin.site.register(Pizza,PizzaAdmin)
admin.site.register(PizzaSize,PizzaAdmin)
admin.site.register(PizzaVariation,PizzaVarityAdmin)
