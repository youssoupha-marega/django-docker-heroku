from django.urls import path

from . import views

#from .views import home

#urlpatterns = [
#    path('', home, name='home'),
#]


urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('formation/', views.formation, name='formation'),
    path('experience/', views.experience, name='experience'),
    path('projet/', views.projet, name='projet'),
    path('contact/', views.contact, name='contact'),
]
