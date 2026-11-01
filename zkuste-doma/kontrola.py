import csv
import sys

from export import DATA, export_mesice, nacti

rok, mesic = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (2026, 10)
prefix = f"{rok:04d}-{mesic:02d}"

with open(DATA, encoding="utf-8", newline="") as f:
    v_datech = {r["cislo"] for r in csv.DictReader(f) if r["datum"].startswith(prefix) and r["kod_slevy"] != "TEST100"}
v_exportu = {r["cislo"] for r in export_mesice(nacti(), rok, mesic)}

print(f"Export za {prefix}: {len(v_exportu)} řádků")
print(f"Přímo v datech:  {len(v_datech)} objednávek (bez testovacích)")
chybi, navic = sorted(v_datech - v_exportu), sorted(v_exportu - v_datech)
if not chybi and not navic:
    print("SEDÍ")
else:
    print("NESEDÍ")
    if chybi:
        print("  chybí v exportu:", ", ".join(chybi))
    if navic:
        print("  navíc v exportu:", ", ".join(navic))
    sys.exit(1)
