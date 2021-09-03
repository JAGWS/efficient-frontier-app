from django.urls import path

from . import views

"""
Hasta ahora, se entra a la aplicación por la dirección que te diga el terminal al ejecutar 
'python manage.py runserver' y te llevará a la página de carga del archivo Excel. Al hacer
click en enviar, se le redirigirá al usuario a la ruta /display. Allí es donde tendrían que
estar los botones y sliders para filtrar las carteras y el gráfico final. 
"""

# app_name = 'eff'
urlpatterns = [
    path("", views.upload, name="upload"),
    path("display", views.display, name="display")
]
