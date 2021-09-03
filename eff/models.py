from django.db import models

# Modelo para guardar los datos clave de cada archivo de Excel. Si se sube un archivo con una lista de 
# activos distinta de las que están ya guardadas, se crea una nueva entrada en la base de datos interna. 
# Si no, se actualiza la entrada existente. 
class InfoActivosModel(models.Model):
    id_mercado = models.TextField() # El id_mercado de cada Excel será una cadena de caracteres con los nombres de todos los activos
    num_activos = models.IntegerField(default=3)
    rentabilidades = models.JSONField() 
    mat_covarianzas = models.JSONField()