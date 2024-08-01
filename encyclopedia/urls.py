from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit/", views.edit_view, name= "edit_view"),
    path("save/", views.save_edit, name="save_edit"),
    path("random/", views.random_searches, name="random_searches"),
]
