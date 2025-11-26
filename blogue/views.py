# blogue/views.py
from django.shortcuts import render

def blogue_acceuil(request):
    # Page de présentation + liste des articles
    articles = [
        {
            "title": "Comment j’ai construit mon portfolio Django",
            "resume": "Je présente les étapes de création de mon site personnel avec Django et Bootstrap.",
            "url_name": "blogue_article_1",
        },
        {
            "title": "Optimiser des modèles de data science en production",
            "resume": "Quelques bonnes pratiques MLOps et monitoring en production.",
            "url_name": "blogue_article_2",
        },
        {
            "title": "Mon parcours de l’UQAM à Nordikeau",
            "resume": "Retour sur mon parcours académique et professionnel.",
            "url_name": "blogue_article_3",
        },
    ]
    return render(request, "blogue/acceuil.html", {"articles": articles})


def blogue_article_1(request):
    return render(request, "blogue/article_1.html")


def blogue_article_2(request):
    return render(request, "blogue/article_2.html")


def blogue_article_3(request):
    return render(request, "blogue/article_3.html")
# blogue/views.py
from django.shortcuts import render

def blogue_acceuil(request):
    # Page de présentation + liste des articles
    articles = [
        {
            "title": "Comment j’ai construit mon portfolio Django",
            "resume": "Je présente les étapes de création de mon site personnel avec Django et Bootstrap.",
            "url_name": "blogue_article_1",
        },
        {
            "title": "Optimiser des modèles de data science en production",
            "resume": "Quelques bonnes pratiques MLOps et monitoring en production.",
            "url_name": "blogue_article_2",
        },
        {
            "title": "Mon parcours de l’UQAM à Nordikeau",
            "resume": "Retour sur mon parcours académique et professionnel.",
            "url_name": "blogue_article_3",
        },
    ]
    return render(request, "blogue/acceuil.html", {"articles": articles})


def blogue_article_1(request):
    return render(request, "blogue/article_1.html")


def blogue_article_2(request):
    return render(request, "blogue/article_2.html")


def blogue_article_3(request):
    return render(request, "blogue/article_3.html")
