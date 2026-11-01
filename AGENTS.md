# Pravidla pro agenty v tomto repozitáři

Šablona z workshopu „Rok, kdy kód psali agenti“ (MAIDAY 2026). Zkopírujte ji do kořene svého repozitáře
a upravte místa označená **[upravte]**. Codex a další agenti čtou `AGENTS.md`, Claude Code čte `CLAUDE.md`,
který sem odkazuje.

## 1. Autor a oponent
- Píšeš kód jako autor. Tvoji změnu zkontroluje druhý agent s jiným zadáním a potom člověk.
- Dělej malé změny s jedním účelem. Co s úkolem nesouvisí, do změny nepatří.
- Smazaný nebo přeskočený test je změna jako každá jiná: napiš ji do reportu.

## 2. Sdílená znalostní báze
- Před prací přečti tento soubor a složku s pravidly **[upravte: např. `docs/pravidla/`]**.
- Když narazíš na chybu, která se může opakovat, navrhni krátký zápis: co se stalo a jak to dělat příště.
  Zápis schvaluje člověk.

## 3. Test odděleně od produkce
- Pracuješ jen v testovacím prostředí **[upravte: název stroje, databáze, URL]**.
- Produkční klíče nemáš a nehledáš je. Když nějaký najdeš, zastav se a ohlas to.
- Nasazení nespouštíš. Připravíš změnu, nasazuje člověk skriptem **[upravte: např. `deploy.sh`]**.

## 4. Strop na náklady
- Každé volání modelu, které přidáš do kódu, má v reportu uvedený model a cenu jednoho volání.
- Levný model první, drahý jen na nejisté případy.
- Po dosažení stropu musí kód hlásit chybu. Žádný tichý přechod na jiný model.

## 5. Čísla se zdrojem
- Každé číslo v reportu má příkaz nebo dotaz, kterým vzniklo, a jde ho spustit znovu.
- Co jsi neověřil, piš jako „neznámo“, nikdy 0.
- „Hotovo“ znamená: uveď příkaz, kterým se to ověří, a jeho výsledek.

## 6. Rozsah doslova
- Dělej jen to, co zadání jmenuje. Krátké „jo“ není souhlas s nasazením ani s ničím dalším.
- U vágního pokynu se zeptej dřív, než začneš.

## Report na konci práce
```
Co se změnilo:        soubory a jednou větou proč
Jak se to ověřilo:    příkazy a jejich výstup
Co zůstává neověřené: výslovně, jinak „nic“
Cena:                 model a cena jednoho volání, pokud se mění
```
