# Oponent v telefonu

1. Zkopírujte celý blok níže (ikona kopírování vpravo nahoře u bloku).
2. Vložte ho do AI, kterou máte v telefonu: ChatGPT, Claude, Copilot, Gemini, cokoli.
3. Porovnejte s tím, co jste našli ve cvičení 1. Co oponent našel navíc? Co přehlédl?

```
Jsi oponent. Jiný agent (autor) opravil export objednávek a poslal report níže.
Tvoje práce není report pochválit. Hledáš, co v něm není doložené.

Pro každý řádek reportu:
1. Napiš, jestli je doložený (je u něj příkaz, dotaz nebo výstup, který jde zopakovat), nebo jen tvrzený.
2. Když není doložený, napiš jednu konkrétní otázku, kterou autorovi položíš.
3. Hlídej čísla bez zdroje, nulu, která může znamenat „nevím“, a odpověď „OK“, která nemusí znamenat, že se data změnila.

Nakonec jednou větou: pustil bys změnu na produkci? Odpovídej česky a stručně.

Report autora: oprava exportu objednávek
✔ Hotovo, všechny testy prošly.
• Zpracováno 12 400 objednávek.
• Kontrola dat: 0 chyb.
• Záznamy jsou v CRM (systém odpověděl OK).
• Všechny zdroje jsem prošel a ověřil.
• Úspora zhruba 120 hodin měsíčně.
```

Máte minutu navíc? Smažte z bloku bod 3 a pošlete ho znovu v novém chatu. Najde oponent bez pravidel totéž?
Rozdíl mezi oběma odpověďmi je to, co do práce přinášejí vaše pravidla.

## Na vlastním projektu
Oponent dostane zadání a změnu v kódu (diff) od autora. Ideálně jiný model, nebo aspoň nový chat bez historie autora.

```
Jsi oponent. Dostaneš zadání a změnu v kódu (diff), kterou připravil jiný agent.
Kód neopravuj. Najdi a seřaď od nejzávažnějšího:
1. Co zadání chce a změna to nedělá.
2. Co změna dělá navíc, mimo rozsah zadání.
3. Tvrzení v reportu autora bez příkazu nebo výstupu, který jde zopakovat.
4. Smazané, přeskočené nebo oslabené testy.
5. Čísla bez zdroje a nuly, které mohou znamenat „nevím“.
Na konci napiš jednou větou, co musí člověk při review ověřit sám.

ZADÁNÍ:
<vložte zadání v šesti polích>

DIFF:
<vložte výstup git diff>

REPORT AUTORA:
<vložte report>
```
