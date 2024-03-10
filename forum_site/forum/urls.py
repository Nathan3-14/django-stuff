from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/create", views.)
    path("<int:post_id>/", views.post_view, name="results")
]
