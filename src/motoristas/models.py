from django.db import models

# Create your models here.

class Motorista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null=True)
    zona = models.CharField(max_length=50, null=False, default="Zona Santiago")

    def get_absolute_url(self):
        return f"/motoristas/{self.id}/"

    def __str__(self):
        return self.nombre + '-' + self.zona
