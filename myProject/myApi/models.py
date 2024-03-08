from django.db import models

# Create your models here.
class Inventory(models.Model):
    itemName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    published_date = models.DateTimeField(auto_now_add=True)
