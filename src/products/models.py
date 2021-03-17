from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)

    def get_absolute_url(self):
        return f"/products/{self.id}/"

    def __str__(self):
        return self.title
