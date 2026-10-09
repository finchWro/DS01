---
name: recenzent-tekstu
description: >-
  Użyj tego skilla, gdy użytkownik prosi o sprawdzenie, ocenę lub recenzję
  fragmentu tekstu pracy (rozdziału, streszczenia, akapitu) pod kątem
  poprawności merytorycznej (technicznej / naukowej), poprawności językowej
  (gramatyka, stylistyka, spójność) oraz literówek i błędów ortograficznych.
  Skill NIE modyfikuje plików źródłowych — wyłącznie ocenia tekst, proponuje
  konkretne poprawki i odsyła do źródeł (artykuły, dokumentacja, podręczniki)
  w celu lepszego zrozumienia tematu przez autora.
---

# Recenzent Tekstu — Skill

Skill służy do profesjonalnej recenzji treści pracy końcowej Data Science
(Politechnika Wrocławska). Agent pełni rolę **recenzenta** — ocenia tekst,
ale **nigdy go samodzielnie nie edytuje**.

> **Zasada nadrzędna:** Skill jest wyłącznie narzędziem oceny i doradztwa.
> Żadna z poniższych procedur nie skutkuje bezpośrednią modyfikacją pliku
> użytkownika. Wszelkie zmiany wprowadza sam autor po zapoznaniu się z
> rekomendacjami.

---

## Kontekst projektu

Przed rozpoczęciem recenzji agent **musi** zapoznać się z kontekstem pracy:

1. Przeczytaj [config.yaml](file:///home/finch/repo/praca-koncowa-zieba/config.yaml)
   — temat, parametry projektu.
2. Przeczytaj [01_tytulowa.md](file:///home/finch/repo/praca-koncowa-zieba/praca/chapters/01_tytulowa.md)
   — pełny tytuł pracy, kierunek, autor.
3. Jeśli recenzowany fragment odwołuje się do danych lub metod, sprawdź
   odpowiednie notebooki w `notebooks/` lub moduły w `src/`.

Kontekst jest konieczny, aby ocena merytoryczna odnosiła się do **konkretnego
tematu pracy**, a nie do ogólnej wiedzy.

---

## Procedura recenzji

### Krok 1: Ustal zakres recenzji

Zapytaj użytkownika (np. przy użyciu narzędzia `ask_question`), jaki zakres
recenzji ma zostać przeprowadzony:

1. **Pełna recenzja** — merytoryka + język + literówki.
2. **Tylko merytoryka** — poprawność techniczna i naukowa.
3. **Tylko język i literówki** — gramatyka, ortografia, stylistyka.

Jeśli użytkownik w swoim zapytaniu już wskazał zakres, potwierdź go i przejdź
do analizy.

---

### Krok 2: Analiza tekstu

Przeczytaj wskazany plik lub fragment za pomocą narzędzia `view_file`.
Przeprowadź analizę w trzech niezależnych wymiarach opisanych poniżej.

---

#### A. Ocena merytoryczna (techniczna / naukowa)

Sprawdź tekst pod kątem:

| Kryterium | Co sprawdzać |
|---|---|
| **Poprawność definicji** | Czy definicje pojęć (np. efektywność spektralna, Massive MIMO, beamforming) są precyzyjne i zgodne z literaturą? |
| **Poprawność wzorów** | Czy wzory matematyczne są poprawne, prawidłowo zapisane w LaTeX i adekwatne do kontekstu (np. wzór Shannona vs. pojemność kanału MIMO)? |
| **Spójność z tematem pracy** | Czy treść bezpośrednio wspiera tezę / cel pracy z tytułu? Czy nie ma dygresji oderwanych od tematu? |
| **Kompletność argumentacji** | Czy nie brakuje kluczowych elementów (np. w streszczeniu: problem, dane, metoda, wynik, wniosek)? |
| **Precyzja terminologiczna** | Czy terminy techniczne są używane poprawnie (np. „matryca anten" vs. „macierz antenowa", „interferencja" vs. „zakłócenia międzyużytkownikowe")? |
| **Adekwatność uproszczeń** | Czy uproszczenia nie zniekształcają sensu (np. opis MIMO jako „dużo anten" bez podania relacji anten vs. użytkowników)? |
| **Poprawność skrótów** | Czy akronimy są prawidłowo rozwinięte przy pierwszym użyciu i spójne w całym tekście? |

Dla każdego znalezionego problemu:
- Opisz, **co jest niepoprawne** i **dlaczego**.
- Zaproponuj **poprawną wersję** (ale NIE edytuj pliku).
- Podaj **źródło** do weryfikacji — link do artykułu, dokumentacji 3GPP,
  podręcznika lub specyfikacji. Preferuj:
  - Specyfikacje 3GPP (np. TS 38.214 dla NR)
  - Podręczniki akademickie (Tse & Viswanath, Goldsmith, Marzetta et al.)
  - Artykuły z IEEE Xplore, arXiv
  - Dokumentacja ITU-R

---

#### B. Ocena językowa (gramatyka, stylistyka, spójność)

Sprawdź tekst pod kątem:

| Kryterium | Co sprawdzać |
|---|---|
| **Poprawność gramatyczna** | Zgodność podmiotu z orzeczeniem, przypadki, szyk zdania. |
| **Styl naukowy** | Czy tekst jest pisany stylem formalnym, bezosobowym (3. osoba lub strona bierna)? Brak kolokwializmów, żargonu. |
| **Spójność wewnętrzna** | Czy zdania logicznie wynikają z siebie? Czy nie ma skoków myślowych? |
| **Zdania urwane / niekompletne** | Czy każde zdanie jest dokończone i ma sens jako samodzielna jednostka? |
| **Powtórzenia** | Czy te same słowa / frazy nie powtarzają się nadmiernie w bliskim sąsiedztwie? |
| **Interpunkcja** | Poprawność użycia przecinków (np. przed „które", „który", „ponieważ"), kropek, myślników. |
| **Konwencja skrótów** | Czy skróty obcojęzyczne używają poprawnego prefiksu? W języku polskim: **ang.** (nie *eng.*), **fr.** (nie *fra.*), itp. |
| **Spójność terminologii** | Czy ten sam termin jest nazywany tak samo w całym tekście (np. nie „wiązka" w jednym miejscu i „beam" w innym bez wyjaśnienia)? |

---

#### C. Ocena ortograficzna (literówki i błędy)

Sprawdź tekst pod kątem:

| Kryterium | Przykłady typowych błędów |
|---|---|
| **Literówki** | „kótry" → „który", „najkłady" → „nakłady", „wykorzytanie" → „wykorzystanie" |
| **Błędy ortograficzne** | „porawiają" → „poprawiają", „efketywność" → „efektywność", „częstotliowsći" → „częstotliwości" |
| **Polskie znaki diakrytyczne** | Brakujące lub nadmiarowe: ą, ę, ć, ś, ź, ż, ó, ł, ń |
| **Zbędne / brakujące spacje** | Podwójne spacje, brak spacji po interpunkcji, spacja przed kropką |

---

### Krok 3: Raport z recenzji

Sporządź raport jako **artefakt markdown** z następującą strukturą:

```markdown
# Recenzja: [nazwa pliku]

## Podsumowanie
- Liczba problemów merytorycznych: X
- Liczba problemów językowych: X
- Liczba literówek / błędów ortograficznych: X

## A. Ocena merytoryczna

### [PROBLEM-M1] Tytuł problemu
- **Lokalizacja:** [link do pliku i linii](file:///ścieżka#Lnr)
- **Opis:** Co jest niepoprawne i dlaczego.
- **Proponowana poprawka:** Sugerowana treść.
- **Źródło:** [Tytuł źródła](URL) — krótki opis, co zweryfikować.

### [PROBLEM-M2] ...

## B. Ocena językowa

### [PROBLEM-J1] Tytuł problemu
- **Lokalizacja:** [link do pliku i linii](file:///ścieżka#Lnr)
- **Tekst oryginalny:** „..."
- **Proponowana poprawka:** „..."
- **Wyjaśnienie:** Dlaczego ta zmiana jest potrzebna.

## C. Literówki i ortografia

| # | Linia | Błąd | Poprawna forma |
|---|-------|------|----------------|
| 1 | L12   | kótry | który          |
| ...                                  |
```

---

### Krok 4: Źródła i materiały dodatkowe

Na końcu raportu **zawsze** dodaj sekcję ze źródłami referencyjnymi, które
pomogą autorowi lepiej zrozumieć tematykę i poprawić tekst:

```markdown
## Rekomendowane źródła

### Źródła merytoryczne
- [Tytuł](URL) — krótki opis, czego dotyczy i do jakiego problemu się odnosi.

### Źródła językowe / redakcyjne
- [Słownik języka polskiego PWN](https://sjp.pwn.pl/) — weryfikacja ortografii.
- [Poradnia językowa PWN](https://sjp.pwn.pl/poradnia) — wątpliwości gramatyczne.
```

---

## Zasady ogólne

1. **NIE edytuj plików użytkownika.** Skill jest recenzentem, nie redaktorem.
   Nigdy nie wywołuj narzędzi `replace_file_content`, `multi_replace_file_content`
   ani `write_to_file` na plikach pracy użytkownika w ramach tego skilla.
2. **Oceniaj w kontekście tematu pracy.** Nie oceniaj tekstu w oderwaniu —
   zawsze odnoś się do tytułu i celu pracy.
3. **Bądź precyzyjny.** Każdy problem musi mieć: lokalizację (plik + linia),
   opis, proponowaną poprawkę i (dla merytoryki) źródło.
4. **Priorytetyzuj problemy.** Na początku raportu umieść najpoważniejsze
   błędy merytoryczne, potem językowe, na końcu literówki.
5. **Język raportu: polski.** Cała komunikacja, raport i rekomendacje
   muszą być w języku polskim (zgodnie z zasadami projektu w `AGENTS.md`).
6. **Wyszukuj źródła.** Użyj narzędzia `search_web`, aby znaleźć aktualne,
   wiarygodne źródła naukowe potwierdzające lub obalające twierdzenia w tekście.
   Preferuj: specyfikacje 3GPP, IEEE, arXiv, podręczniki akademickie.
