from django.db import models
from decimal import Decimal

# Create your models here.

class Order(models.Model):
    """Stores order information"""
    orderStatus = (("progress","progress"),("paid","paid"),("completed","completed"),("cancelled","cancelled"))
    status = models.CharField(max_length=32,choices=orderStatus,default="progress")
    customer_name = models.CharField(max_length=128)
    customer_address = models.CharField(max_length=300)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal(0.00))

    def __str__(self):
        return "%s - %s" %(self.customer_name,self.total)

class OrderItems(models.Model):
    "stores information about orderd items"

    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    pizza =models.ForeignKey('pizzaApp.Pizza',on_delete=models.SET_NULL,related_name='orders',null=True)
    size = models.ForeignKey('pizzaApp.PizzaSize',on_delete=models.SET_NULL,related_name='orders',null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return  "%s %s %s %s" %(self.pizza,self.quantity,self.size,self.price)


from django.apps import apps
from django.db.models import Sum

def order_pre_save(sender,instance,**kwargs):
    """to be excuted before creating actually order"""
    PizzaVarity = apps.get_model('pizzaApp','PizzaVariation')
    variation = PizzaVarity.objects.get(pizza=instance.pizza,size=instance.size)
    instance.price = instance.quantity*variation.price

def order_post_save(sender,instance,**kwargs):
    """to be excuted before creating actually order, this will also calculate total price"""
    order = instance.order
    amount = order.items.aggregate(Sum('price'))
    if amount and amount['price__sum']:
        order.save()


models.signals.pre_save.connect(order_pre_save,sender=OrderItems)
models.signals.post_save.connect(order_post_save,sender=OrderItems)