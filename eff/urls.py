from django.urls import path

from . import views

app_name = 'eff'
urlpatterns = [
    path("", views.index, name="index")
]