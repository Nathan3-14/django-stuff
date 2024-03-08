from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name-test/", views.name, name="Name")
]
