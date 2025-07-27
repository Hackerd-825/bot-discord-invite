#!/bin/bash

echo "🚀 Lancement du script d'installation pour le Bot Discord"

# Mettre à jour les paquets
echo "🔄 Mise à jour des paquets..."
sudo apt update -y && sudo apt upgrade -y

# Installer Python3 et pip3
echo "🐍 Vérification de Python et pip..."
sudo apt install -y python3 python3-pip

# Installer les dépendances Python
echo "📦 Installation des dépendances Python..."
pip3 install -r requirements.txt

# Créer le dossier log si pas déjà présent
echo "📁 Création du dossier log..."
mkdir -p log

# Créer les fichiers de log vides
touch log/sent.txt log/accepted.txt log/not_accepted.txt

# Donner les droits d'exécution au script de lancement Linux
chmod +x start.sh

echo "✅ Installation terminée !"
echo "Pour démarrer le bot : ./start.sh"
