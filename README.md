# Agenti a pravidla

Materiály k workshopu **Rok, kdy kód psali agenti** (MAIDAY 2026, Mendelova univerzita v Brně, 4. 11. 2026).
Vede Jan Polišenský, CTO Lakmoos AI a lektor ICT Pro ([janpoli.com](https://janpoli.com)).

Žádný firemní kód ani data. Všechno smíte zkopírovat a upravit pro svou firmu.

## Na workshopu: oponent v telefonu
Otevřete **[oponent.md](oponent.md)**, zkopírujte blok do AI v telefonu a porovnejte, co najde, s tím,
co jste našli ve cvičení 1.

## Co tu je
| Soubor | K čemu |
|---|---|
| [AGENTS.md](AGENTS.md) | Šest pravidel jako soubor, který váš agent čte před prací. Zkopírujte do kořene svého repozitáře. |
| [CLAUDE.md](CLAUDE.md) | Odkaz na `AGENTS.md` pro Claude Code. |
| [zadani-sablona.md](zadani-sablona.md) | Zadání pro agenta v šesti polích, šablona a vzor. |
| [oponent.md](oponent.md) | Prompt pro druhého agenta, který hledá chyby autora. Verze pro workshop i pro vlastní projekt. |
| [limity.md](limity.md) | Klíče, stropy a varování, aby se kredity nepropálily. Kontrolní seznam. |
| [zkuste-doma/](zkuste-doma/ULOHA.md) | Malý projekt na 15 minut: stejný úkol s vágním zadáním a v šesti polích. |

## Šest pravidel
1. **Autor a oponent.** Jeden agent píše, druhý s vlastními instrukcemi hledá chyby. Člověk čte každou změnu, malou a s jedním účelem.
2. **Sdílená znalostní báze.** Pravidla a poučení v jedné složce (repozitáři), kterou čte každý agent.
3. **Test odděleně od produkce.** Agenti nemají produkční klíče. Nasazuje člověk připraveným skriptem.
4. **Strop na náklady.** Klíč a strop pro každé prostředí, cena za volání v každém reportu.
5. **Čísla se zdrojem.** Každé číslo spočítal skript, který jde spustit znovu. Co chybí, je „neznámo“, ne nula.
6. **Rozsah doslova.** Agent dělá jen to, co zadání jmenuje. U vágního pokynu se zeptá.

## Pokračování
Chcete stejný workshop pro svůj tým, nebo navázat online? Napište na polisensky.john@gmail.com.
