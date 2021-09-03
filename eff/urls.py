from django.urls import path

from . import views

# app_name = 'eff'
urlpatterns = [
    path("", views.upload, name="upload"),
    path("display", views.display, name="display")
]
