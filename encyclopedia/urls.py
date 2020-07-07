from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.content,name="content"),
    path("edit/<str:title>",views.edit,name="edit"),
    path("add",views.add,name="add"),
    path("rand",views.rand,name="rand"),
]
