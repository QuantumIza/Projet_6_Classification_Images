import sys
import os

def initialize_environment():
    # 📁 Monter le Drive si nécessaire
    if not os.path.exists('/content/drive'):
        from google.colab import drive
        drive.mount('/content/drive')

    # 📦 Installer les dépendances
    requirements_path = '/content/drive/MyDrive/Projet_6_Classification_Images/requirements.txt'
    if os.path.exists(requirements_path):
        print("📦 Installation des dépendances...")
        os.system(f'pip install -r {requirements_path}')
    else:
        print("⚠️ Fichier requirements.txt introuvable.")

    # 📂 Ajouter le dossier src au path
    src_path = '/content/drive/MyDrive/Projet_6_Classification_Images/src'
    if src_path not in sys.path:
        sys.path.append(src_path)
        print(f"📂 Dossier ajouté au path : {src_path}")
    else:
        print("📂 Dossier src déjà dans le path.")

    # 🔍 Afficher les versions installées
    try:
        import tensorflow as tf
        import sklearn
        import pandas as pd
        import matplotlib
        import numpy as np

        print("✅ TensorFlow:", tf.__version__)
        print("✅ scikit-learn:", sklearn.__version__)
        print("✅ pandas:", pd.__version__)
        print("✅ matplotlib:", matplotlib.__version__)
        print("✅ numpy:", np.__version__)
    except ImportError as e:
        print("⚠️ Erreur d'importation :", e)
