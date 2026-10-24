# Amazon Scraper (Selenium + SQLite)

Scrape les résultats de recherche d'Amazon.fr avec Selenium et stocke les produits dans une base SQLite. Architecture MVC.

## Installation

```bash
cd amazon_scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Google Chrome (ou Edge) doit être installé.

Par défaut (`BACKEND = "cdp"` dans `config.py`), le projet pilote directement ton Chrome via son port de débogage : aucun `chromedriver.exe` n'est téléchargé, ce qui évite les blocages Windows (Smart App Control, `WinError 4551`). Mets `BACKEND = "selenium"` pour utiliser Selenium classique.

## Utilisation

```bash
python main.py                         # menu interactif
python main.py scrape "clavier" -p 3   # scrape 3 pages
python main.py scrape "souris" --headless
python main.py tech -p 2               # toute la catégorie tech + sous-catégories -> CSV
python main.py tech -c Informatique    # une seule catégorie
python main.py list                    # affiche les produits en base
python main.py search "logitech"       # recherche dans la base
python main.py export                  # CSV + JSON dans exports/
```

## Structure

```
amazon_scraper/
├── main.py                  # point d'entrée (CLI + menu)
├── config.py                # paramètres (URL, délais, chemins)
├── models/produit.py        # dataclass Produit + ProduitRepository (SQLite)
├── scraper/
│   ├── amazon_scraper.py    # pilotage Selenium (navigation, pagination)
│   └── parsing.py           # extraction/nettoyage des champs d'une carte
├── controllers/
│   └── scraping_controller.py
├── views/
│   ├── console_view.py      # affichage terminal
│   └── export_view.py       # export CSV / JSON
├── data/produits.db         # base SQLite (créée automatiquement)
└── exports/                 # fichiers exportés
```

## Catégorie tech

Les catégories et sous-catégories sont définies dans `config.py` (`TECH_CATEGORIES`) : chaque sous-catégorie est lancée comme une recherche Amazon, sur `TECH_PAGES` pages. Les produits sont sauvegardés en base au fil de l'eau, puis un fichier `exports/tech_AAAAMMJJ_HHMMSS.csv` (séparateur `;`, colonnes `categorie` et `sous_categorie` incluses) est généré à la fin, même si un captcha interrompt le scraping.

## Base de données

Table `produits` : `asin` (unique), `titre`, `prix`, `note`, `nb_avis`, `url`, `image_url`, `requete`, `categorie`, `sous_categorie`, `date_scraping`.
Un produit déjà présent (même ASIN) est mis à jour, pas dupliqué.

## Notes

- Amazon peut afficher un captcha si tu scrapes trop vite : garde des délais (`DELAY_MIN/MAX`) et peu de pages.
- Les sélecteurs CSS d'Amazon changent parfois : ils sont regroupés dans `scraper/parsing.py` pour être faciles à ajuster.
- Vérifie les conditions d'utilisation d'Amazon et n'utilise ce projet qu'à des fins d'apprentissage / personnelles.
