# -*- coding: utf-8 -*-
"""
POINT D'ENTRÉE :  python main.py

Architecture MVC du projet :
    models/       (M) les DONNÉES et la LOGIQUE : lire, nettoyer, rapprocher, comparer. Ne contient aucun print.
    views/        (V) l'AFFICHAGE : écran (console_view) et fichiers (fichiers_view). Ne contient aucun calcul.
    controllers/  (C) le CHEF D'ORCHESTRE : appelle les modèles dans l'ordre, passe les résultats aux vues.
    config.py         les réglages (chemins, enseignes, panier, dates).
"""
from controllers.analyse_controller import AnalyseController

if __name__ == "__main__":
    AnalyseController().lancer()
