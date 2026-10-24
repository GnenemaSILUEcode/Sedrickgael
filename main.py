"""Point d'entrée.

Usage :
    python main.py                          -> menu interactif
    python main.py scrape "clavier" -p 3    -> scrape 3 pages et stocke en base
    python main.py tech -p 2                -> scrape toute la catégorie tech + CSV
    python main.py list                     -> liste les produits
    python main.py search "logitech"        -> recherche dans la base
    python main.py export                   -> export CSV + JSON
"""
import argparse

import config
from controllers.scraping_controller import ScrapingController
from views import console_view


def interactif(ctrl: ScrapingController) -> None:
    while True:
        choix = console_view.menu()
        if choix == "1":
            q = input("Recherche : ").strip()
            if not q:
                continue
            p = input(f"Nombre de pages [{config.MAX_PAGES}] : ").strip()
            ctrl.scraper(q, int(p) if p.isdigit() else config.MAX_PAGES)
        elif choix == "2":
            ctrl.lister()
        elif choix == "3":
            ctrl.rechercher(input("Mot-clé : ").strip())
        elif choix == "4":
            ctrl.exporter()
        elif choix == "5":
            if input("Vider la base ? (o/N) ").lower() == "o":
                ctrl.vider()
        elif choix == "6":
            p = input(f"Pages par sous-catégorie [{config.TECH_PAGES}] : ").strip()
            ctrl.scraper_tech(int(p) if p.isdigit() else config.TECH_PAGES)
        elif choix == "0":
            break
        else:
            console_view.erreur("Choix invalide.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Amazon scraper (Selenium + SQLite)")
    sub = parser.add_subparsers(dest="cmd")

    s = sub.add_parser("scrape", help="scraper une recherche")
    s.add_argument("query")
    s.add_argument("-p", "--pages", type=int, default=config.MAX_PAGES)
    s.add_argument("--headless", action="store_true", help="navigateur invisible")

    t = sub.add_parser("tech", help="scraper la catégorie tech et ses sous-catégories")
    t.add_argument("-p", "--pages", type=int, default=config.TECH_PAGES)
    t.add_argument("--headless", action="store_true")
    t.add_argument("-c", "--categorie", action="append",
                   help="limiter à une catégorie (répétable), ex : -c Informatique")

    sub.add_parser("list", help="lister les produits en base")
    q = sub.add_parser("search", help="rechercher dans la base")
    q.add_argument("mot_cle")
    sub.add_parser("export", help="exporter en CSV + JSON")

    args = parser.parse_args()
    ctrl = ScrapingController()

    if args.cmd == "scrape":
        ctrl.scraper(args.query, args.pages, headless=args.headless or config.HEADLESS)
    elif args.cmd == "tech":
        ctrl.scraper_tech(args.pages, headless=args.headless or config.HEADLESS,
                          categories=args.categorie)
    elif args.cmd == "list":
        ctrl.lister()
    elif args.cmd == "search":
        ctrl.rechercher(args.mot_cle)
    elif args.cmd == "export":
        ctrl.exporter()
    else:
        interactif(ctrl)


if __name__ == "__main__":
    main()
