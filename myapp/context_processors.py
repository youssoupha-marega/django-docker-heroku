# myapp/context_processors.py

def menu_items(request):
    return {
        'menu_items': [
            {"name": "acceuil", "label": "Acceuil"},
            {"name": "formation", "label": "Formation"},
            {"name": "experience", "label": "Experience"},
            {"name": "projet", "label": "Projet"},
            {"name": "blogue_acceuil", "label": "Blogue"},
            {"name": "contact", "label": "Contact"}
        ]
    }
