#!/usr/bin/env bash
# Arrêter en cas d'erreur
set -o errexit

# Installer les dépendances Python
pip install -r requirements.txt

# Construire Tailwind (si nécessaire)
python manage.py tailwind build || echo "Tailwind build failed, continuing..."

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Appliquer les migrations
python manage.py migrate

