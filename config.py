"""Configuration globale du projet."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
DB_PATH = os.path.join(DATA_DIR, "produits.db")

BASE_URL = "https://www.amazon.fr"
SEARCH_URL = BASE_URL + "/s?k={query}&page={page}"

HEADLESS = False          # True = navigateur invisible
PAGE_TIMEOUT = 15         # secondes d'attente max pour un élément
DELAY_MIN = 2.0           # pause aléatoire entre deux pages (secondes)
DELAY_MAX = 5.0
MAX_PAGES = 2             # pages par recherche (par défaut)

# "cdp"      : pilote ton Chrome/Edge directement (aucun chromedriver.exe)
# "selenium" : Selenium classique (télécharge chromedriver.exe)
BACKEND = "cdp"
CHROME_PATH = ""          # optionnel : chemin de chrome.exe si non trouvé automatiquement

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

# Catégorie tech -> sous-catégories (chaque sous-catégorie = une recherche Amazon).
# Modifie / complète librement cette liste.
TECH_CATEGORIES = {
    "Informatique": [
        "ordinateur portable", "pc de bureau", "ecran pc", "clavier", "souris",
        "imprimante", "disque dur externe", "ssd", "carte graphique",
        "routeur wifi", "tablette tactile",
    ],
    "High-Tech": [
        "smartphone", "casque audio", "ecouteurs bluetooth", "enceinte bluetooth",
        "montre connectee", "television", "appareil photo", "drone",
        "camera de surveillance",
    ],
    "Jeux video": [
        "console de jeux", "manette de jeu", "casque gaming",
    ],
    "Accessoires": [
        "chargeur rapide", "cable usb-c", "batterie externe", "coque smartphone",
        "hub usb",
    ],
}
TECH_PAGES = 2            # pages par sous-catégorie
