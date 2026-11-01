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
CÍL:      Export za zvolený měsíc vrací všechny objednávky, i ty se slevou. Testovací objednávky v něm nejsou.
ROZSAH:   Jen modul exportu. Formát výstupu a rozhraní funkcí beze změny.
NESMÍ:    Sahat na produkci, spouštět nasazení, mazat data, měnit klíče a konfiguraci.
HOTOVO:   Testy projdou a počet řádků exportu sedí s přímým počtem v datech (kontrola.py).
NASAZUJE: Člověk, připraveným skriptem, po review.
OPONENT:  Jiný model zkontroluje změnu proti tomuto zadání a hledá, co autor vynechal.
```
