from django.urls import path

from . import views

#from .views import home

#urlpatterns = [
#    path('', home, name='home'),
#]


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
