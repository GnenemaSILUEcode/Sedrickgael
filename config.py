# -*- coding: utf-8 -*-
"""
CONFIG : tous les réglages au même endroit (chemins, noms des enseignes, panier, dates).
Si l'énoncé change (autre panier, autre semaine), on ne modifie que ce fichier.
"""
import os

DOSSIER_PROJET = os.path.dirname(os.path.abspath(__file__))
DOSSIER_DONNEES = os.path.join(DOSSIER_PROJET, "donnees")
DOSSIER_RESULTATS = os.path.join(DOSSIER_PROJET, "resultats")

# Noms écrits EXACTEMENT comme dans historique_prix.csv (colonne "source")
ML = "Marché Lagune"
BB = "Baobab Shop"
CI = "Comptoir Ivoire"
ENSEIGNES = [ML, BB, CI]

# Panier de rentrée : produit_id -> quantité
PANIER = {"P04": 1, "P12": 1, "P14": 2, "P15": 1, "P28": 1}

# Semaine du Black Friday 2025 (dates AAAA-MM-JJ : elles se comparent comme du texte)
BF_DEBUT = "2025-11-24"
BF_FIN = "2025-11-30"
