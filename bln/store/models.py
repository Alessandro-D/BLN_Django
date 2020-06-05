from django.db import models

# Create your models here.

class InvoiceCounter(models.Model):
    count = models.IntegerField()