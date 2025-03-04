FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


#COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Copie des fichiers dans le conteneur
COPY . /app

# Exposer le port 8000
EXPOSE 8000

# Lancer le serveur avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi"]
