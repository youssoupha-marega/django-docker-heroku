# Utilisation d'une image légère Python 3.12.2 slim
FROM python:3.12.2-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers dans le conteneur
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt




#COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




# Exposer le port 8000
#EXPOSE 8000

# Lancer le serveur avec Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi"]
