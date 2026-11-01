# Zadání pro agenta v šesti polích

Vágní zadání je pozvánka k domýšlení. Šest polí stačí, aby šlo pochopit jen jedním způsobem.
Zadání ukládejte do souboru, ne jen do chatu: zůstane záznam, co se chtělo.

| Pole | Otázka |
|---|---|
| **CÍL** | Co má platit, až bude hotovo? |
| **ROZSAH** | Na co agent smí sáhnout? |
| **NESMÍ** | Co agent dělat nesmí? |
| **HOTOVO** | Jakým příkazem nebo kontrolou se to ověří? |
| **NASAZUJE** | Kdo a jak? |
| **OPONENT** | Kdo práci zkontroluje a podle čeho? |

Nejčastěji chybí řádek NESMÍ. Bez něj agent udělá víc, než jste chtěli.

## Šablona ke zkopírování
```
CÍL:
ROZSAH:
NESMÍ:
HOTOVO:
NASAZUJE:
OPONENT:
```

## Vzor z workshopu
Původní zadání od šéfa: „Oprav ten export objednávek a nasaď to.“ V exportu chybí objednávky se slevou.

```
CÍL:      Export za zvolený měsíc vrací všechny objednávky, i ty se slevou.
ROZSAH:   Jen modul exportu. Schéma databáze a API beze změny.
NESMÍ:    Sahat na produkci, spouštět nasazení, mazat data a měnit klíče.
HOTOVO:   Test na testovacích datech projde a počet řádků sedí s dotazem do databáze.
NASAZUJE: Člověk, připraveným skriptem, po review.
OPONENT:  Jiný model zkontroluje změnu proti zadání a hledá, co autor vynechal.
```

Stejné zadání upravené pro cvičný projekt (data v CSV, místo dotazu do databáze `kontrola.py`) je
v [zkuste-doma/ULOHA.md](zkuste-doma/ULOHA.md).
