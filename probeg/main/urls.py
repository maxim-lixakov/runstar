from django.urls import path
from . import views

urlpatterns = [
    path('results', views.results),
    path('find', views.unique_users),
    path('about', views.about),
    path('contact', views.contact),
    path('', views.home)
]