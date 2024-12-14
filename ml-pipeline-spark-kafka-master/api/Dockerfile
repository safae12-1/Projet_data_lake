# Utiliser une image Python officielle
FROM python:3.9-slim


# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt --timeout=120

# Copier l'application et les données
COPY api.py .
COPY mental_health_and_technology_usage_2024.csv .

# Installer uvicorn
RUN pip install uvicorn

# Exposer le port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--reload"]