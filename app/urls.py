from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("amazon/", views.amazon, name="amazon"),
]
