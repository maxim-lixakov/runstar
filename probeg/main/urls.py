from django.urls import path
from . import views, authed_views

urlpatterns = [
    path('results', views.results),
    path('find', views.unique_users),
    path('about', views.about),
    path('contact', views.contact),
    path('robots.txt', views.robots),
    path('signup', authed_views.SignUp.as_view(), name='signup'),
    path('profile', authed_views.profile),
    path('', views.home, name='home')
]