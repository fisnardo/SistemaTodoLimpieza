from django.db import models

# Create your models here.

class productos(models.Model):
    nombre_prod = models.CharField(max_length=250)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2)
    stock_disp = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=250)
