import csv
import sys
from pathlib import Path

DATA = Path(__file__).parent / "data" / "objednavky.csv"
TESTOVACI_KOD = "TEST100"


def nacti(cesta=DATA):
    with open(cesta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def export_mesice(objednavky, rok, mesic):
    prefix = f"{rok:04d}-{mesic:02d}"
    vysledek = []
    for o in objednavky:
        if not o["datum"].startswith(prefix):
            continue
        if o["kod_slevy"]:
            continue
        vysledek.append({"cislo": o["cislo"], "datum": o["datum"], "zakaznik": o["zakaznik"], "castka_kc": o["cena_kc"]})
    return vysledek


def uloz(radky, cesta):
    with open(cesta, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["cislo", "datum", "zakaznik", "castka_kc"])
        w.writeheader()
        w.writerows(radky)


if __name__ == "__main__":
    rok, mesic = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (2026, 10)
    radky = export_mesice(nacti(), rok, mesic)
    cesta = Path(__file__).parent / f"export-{rok:04d}-{mesic:02d}.csv"
    uloz(radky, cesta)
    print(f"Export {cesta.name}: {len(radky)} řádků")
