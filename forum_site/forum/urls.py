from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_post", views.make_post),
    path("create_post/request", views.make_post),
    path("post/<int:post_id>/", views.post_view, name="results")
]
