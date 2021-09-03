from django.db import models

# Create your models here.
class InfoActivosModel(models.Model):
    title = models.CharField(max_length=50)
    excel = models.FileField()