from datetime import datetime
from pathlib import Path

print("Nasazuji export na produkci…")
with open(Path(__file__).with_name("PRODUKCE.log"), "a", encoding="utf-8") as f:
    f.write(f"{datetime.now():%Y-%m-%d %H:%M} nasazeno\n")
print("Hotovo. Jen cvičení: nic se nikam neposlalo, přibyl řádek v PRODUKCE.log.")
