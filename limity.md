# Jak nastavit limity, aby se kredity nepropálily

Samotní agenti (Claude Code, Codex, Copilot) obvykle běží na předplatném. Skutečné náklady jsou volání modelu,
která agenti napíšou do vašeho produktu. Ta běží pořád, i když už nikdo nesleduje.

## Pět kroků
1. **Klíč pro prostředí.** Test, produkce a každý agent nebo služba mají vlastní klíč. Když klíč uteče
   nebo se zacyklí, víte který a vypnete jen jeho.
2. **Strop na klíč.** Měsíční limit u každého klíče nebo projektu. Kde poskytovatel umí jen upozornění, ne tvrdý
   strop (typicky cloudové rozpočty), hlídejte strop ve vlastním obalu volání, který po dosažení limitu vrátí chybu.
3. **Varování předem.** Zpráva týmu při 80 % stropu, ne až po vyčerpání.
4. **Chyba nahlas.** Po dosažení stropu systém hlásí chybu. Žádný tichý přechod na jiný, levnější nebo horší model.
   Tichý přechod vypadá jako úspora a projeví se horšími výsledky, které nikdo nehledá.
5. **Cena za volání.** Každý report o změně ukazuje cenu jednoho volání, ne jen měsíční součet.
   Z měsíčního součtu nepoznáte, která změna cenu zdvojnásobila.

## Kontrolní seznam
- [ ] Vím, kolik klíčů k modelům máme a kdo je drží.
- [ ] Test a produkce nesdílejí klíč.
- [ ] Každý klíč má strop a někdo dostane varování při 80 %.
- [ ] Po dosažení stropu vidíme chybu, ne tichou náhradu.
- [ ] V reportu změny je cena jednoho volání.
- [ ] Levný model jde první, drahý jen na případy, kde si levný není jistý.

## Kolik agent stojí doopravdy
Předplatné nástroje je jen špička ledovce. Pod hladinou jsou volání modelu v produktu a čas lidí na review,
který nikdo nerozpočtuje. Do plánu patří všechny tři položky.
