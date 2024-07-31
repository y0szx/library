from . import views
from django.urls import path
from django.urls.resolvers import URLPattern


urlpatterns: list[URLPattern] = [
    path('', views.book_list, name='book_list'),
]
