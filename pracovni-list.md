# Pracovní list: Rok, kdy kód psali agenti

MAIDAY 2026, workshop 4. 11. 2026. Pracujte ve dvojicích u jednoho notebooku. Odpovědi pište přímo sem:
zkopírujte si soubor do editoru (tlačítko Raw, nebo `git clone`), nebo do vlastních poznámek.
Prezentace, tento list v PDF a tahák s řešením jsou ve složce [prezentace/](prezentace/).

## Cvičení 1: Odkud je to číslo? (4 min)

Agent poslal tenhle report. U každého řádku rozhodněte: přijmete ho, nebo se zeptáte? Když se zeptáte,
napište otázku, kterou agentovi položíte. Report je smyšlený, každý typ chyby v něm ale opravdu nastal.

```
Report agenta: oprava exportu objednávek

✔ Hotovo, všechny testy prošly.
Zpracováno 12 400 objednávek.
Kontrola dat: 0 chyb.
Záznamy jsou v CRM (systém odpověděl OK).
Všechny zdroje jsem prošel a ověřil.
Úspora zhruba 120 hodin měsíčně.
```

| Řádek reportu | Přijmu, nebo se zeptám? | Moje otázka pro agenta |
|---|---|---|
| Hotovo, všechny testy prošly. | | |
| Zpracováno 12 400 objednávek. | | |
| Kontrola dat: 0 chyb. | | |
| Záznamy jsou v CRM (systém odpověděl OK). | | |
| Všechny zdroje jsem prošel a ověřil. | | |
| Úspora zhruba 120 hodin měsíčně. | | |

## Cvičení 2: Kdo smí co (4 min)

Ke každému úkolu napište **A** (agent sám: smí bez schválení), **Č** (člověk čte: agent připraví, člověk přečte,
než to platí), nebo **J** (jen člověk: provede člověk, agent smí připravit podklad).

| # | Úkol | A / Č / J |
|---|---|---|
| 1 | Projít kód a navrhnout opravu chyby | |
| 2 | Napsat a pustit testy na testovacím stroji | |
| 3 | Sloučit pull request do main | |
| 4 | Nasadit novou verzi na produkci | |
| 5 | Poslat klientovi souhrn výsledků | |
| 6 | Smazat stará data z databáze | |
| 7 | Připravit koncept nabídky | |
| 8 | Změřit výkon nové verze na testu | |
| 9 | Zveřejnit číslo v týmovém kanálu | |
| 10 | Vytvořit nový API klíč pro produkci | |
| 11 | Napsat zprávu jménem kolegy | |
| 12 | Shrnout dokumentaci | |

Kde jsme se ve dvojici neshodli a proč:



## Cvičení 3: Zadání pro agenta (5 min)

Šéf napsal agentovi: „Oprav ten export objednávek a nasaď to.“ Kontext: v exportu chybí objednávky se slevou.
Přepište zadání do šesti polí tak, aby ho agent nemohl pochopit špatně. U HOTOVO napište, jakým příkazem
nebo kontrolou se to ověří.

```
CÍL:
ROZSAH:
NESMÍ:
HOTOVO:
NASAZUJE:
OPONENT:
```

Pak si vyzkoušejte oponenta: [oponent.md](oponent.md).

## Cvičení 4: Váš plán na pondělí (4 min)

Šest pravidel, ke kterým jsme došli. Vyberte tři, která vaše firma zatím nemá, a ke každému napište vlastníka
a první krok. První krok musí jít udělat do pátku 13. 11.

1. **Autor a oponent.** Jeden agent píše, druhý hledá chyby. Člověk čte každou změnu, malou a s jedním účelem.
2. **Sdílená znalostní báze.** Pravidla a poučení v jednom repu (AGENTS.md), které čte každý agent.
3. **Test odděleně od produkce.** Agenti nemají produkční klíče. Nasazuje člověk připraveným skriptem.
4. **Strop na náklady.** Klíč a strop pro každé prostředí, cena za volání v každém reportu.
5. **Čísla se zdrojem.** Každé číslo spočítal skript, který jde spustit znovu. Co chybí, je „neznámo“, ne nula.
6. **Rozsah doslova.** Agent dělá jen to, co zadání jmenuje. U vágního pokynu se zeptá.

| Pravidlo | Vlastník | První krok | Hotovo do |
|---|---|---|---|
| Vzor: test odděleně od produkce | vedoucí IT | zjistit, kdo má produkční klíče a kde leží | 13. 11. |
| | | | |
| | | | |
| | | | |

„Zavést governance“ není krok. „Zjistit, kdo má produkční klíče a kde leží“ je krok.
