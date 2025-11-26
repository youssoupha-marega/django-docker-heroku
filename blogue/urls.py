# blogue/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogue_acceuil, name='blogue_acceuil'),  # /blogue/
    path('article-1/', views.blogue_article_1, name='blogue_article_1'),
    path('article-2/', views.blogue_article_2, name='blogue_article_2'),
    path('article-3/', views.blogue_article_3, name='blogue_article_3'),
]
