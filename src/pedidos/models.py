from django.db import models
from django.contrib.auth.models import User
from motoristas.models import Motorista
from products.models import Product



# Create your models here.

class Pedido(models.Model):
    comprador_id = models.ForeignKey(User, on_delete=models.CASCADE)
    motorista_id = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
