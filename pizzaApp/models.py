from django.db import models

# Create your models here.

class PizzaSize(models.Model):
    """ information about pizza size"""
    size = models.IntegerField(unique=True,help_text="cm")

    def __str__(self):
        return "%s cm" %self.size

class Pizza(models.Model):
    """ stored pizza name """
    name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return  self.name

class PizzaVariation(models.Model):
    """stores avaliable variation for each pizza"""
    pizza =models.ForeignKey(Pizza,related_name="variation",on_delete=models.CASCADE)
    size =models.ForeignKey(PizzaSize,related_name="size_variation",on_delete=models.SET_NULL,null=True)
    price =models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        unique_together = ('pizza','size')
