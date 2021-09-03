from django.db import models

# Create your models here.
class InfoActivosModel(models.Model):
    id_mercado = models.TextField()
    rentabilidades = models.JSONField()
    volatilidades = models.JSONField()