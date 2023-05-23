from django.urls import path
from django.views.generic.base import TemplateView

from . import views, authed_views

urlpatterns = [
    path('results', views.results),
    path('find', views.unique_users),
    path('about', views.about),
    path('contact', views.contact),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path('signup', authed_views.SignUp.as_view(), name='signup'),
    path('profile', authed_views.profile),
    path('', views.home, name='home')
]

