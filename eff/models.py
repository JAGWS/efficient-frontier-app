from django.db import models

# Create your models here.
class InfoActivosModel(models.Model):
    id_mercado = models.TextField()
    num_activos = models.IntegerField(default=3)
    rentabilidades = models.JSONField()
    volatilidades = models.JSONField()