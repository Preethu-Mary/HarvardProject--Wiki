from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("<str:title>/edit", views.edit, name="edit"),
    path("save_changes", views.save_changes, name="save_changes"),
    path("random_choice", views.random_choice, name="random_choice"),
    path("<str:title>", views.entry_page, name="entry")
]
