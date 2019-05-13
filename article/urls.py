from django.urls import path,re_path

from . import views

urlpatterns=[
    path("<int:article_id>/", views.article_detail, name="article_detail"),
    path("", views.article_list, name="article_list"),
    path("type", views.article_types, name="article_types"),
    path("type/<int:type_id>", views.article_type, name="article_type"),

]
