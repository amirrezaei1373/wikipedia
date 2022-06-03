from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/" , views.home, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("random/", views.get_random, name="get_random")
]
