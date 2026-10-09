---
name: zarzadzanie-referencjami
description: >-
  Użyj tego skilla, gdy użytkownik chce dodać nową pozycję bibliograficzną (artykuł naukowy,
  raport techniczny np. 3GPP, specyfikację, książkę, stronę WWW/dokumentację) do pliku
  praca/references.bib oraz dowiedzieć się, jak prawidłowo zacytować ją w tekście pracy
  (w formacie Markdown/Pandoc [@klucz] lub LaTeX \cite{klucz}).
---

# Zarządzanie Referencjami — Skill

Skill odpowiada za automatyczne, standaryzowane dodawanie źródeł bibliograficznych do pliku [references.bib](file:///home/finch/repo/praca-koncowa-zieba/praca/references.bib) oraz instruowanie użytkownika, w jaki sposób wstawiać cytowania w tekście rozdziałów (`praca/chapters/*.md`).

---

## Cele i zadania skilla

1. **Pobranie i weryfikacja metadanych źródła:**
   - Na podstawie linku URL, identyfikatora DOI, numeru raportu 3GPP/specyfikacji lub opisu publikacji agent pobiera (narzędziami `read_url_content`, `search_web`) pełne metadane: autorów, tytuł, rok, wydawcę, tom/zeszyt/strony, organizację, URL i datę dostępu.
2. **Generowanie czystego i unikalnego klucza BibTeX:**
   - Schemat klucza: czytelny, zwięzły, jednoznaczny (np. `NazwiskoRok`, `3gpp_tr38843`, `autor_rok_slowo`).
   - Sprawdzenie, czy klucz nie koliduje z istniejącymi wpisami w [references.bib](file:///home/finch/repo/praca-koncowa-zieba/praca/references.bib).
3. **Wybór właściwego typu wpisu BibTeX:**
   - `@article` — dla artykułów z czasopism naukowych (IEEE, Springer, Elsevier itp.).
   - `@inproceedings` — dla referatów konferencyjnych i warsztatowych (np. IEEE ICC, Globecom, ITA).
   - `@techreport` / `@standard` — dla raportów technicznych i specyfikacji (np. 3GPP TR/TS, ITU-R, ETSI, IETF RFC).
   - `@book` — dla książek i podręczników akademickich.
   - `@online` / `@misc` — dla stron internetowych, dokumentacji technicznej, repozytoriów danych i wpisów na portalach branżowych (np. ShareTechNote).
4. **Aktualizacja pliku `praca/references.bib`:**
   - Poprawne dopisanie nowego wpisu na końcu pliku z zachowaniem formatowania i kodowania UTF-8.
5. **Prezentacja instrukcji wstawienia do tekstu:**
   - Wyjaśnienie autorowi, jak zacytować nowo dodaną pozycję w plikach rozdziałów Markdown oraz w LaTeX.

---

## Procedura krok po kroku

### Krok 1: Identyfikacja i zebranie metadanych

- Jeśli podano URL: użyj `read_url_content`, by odczytać stronę i wyciągnąć metadane (tytuł, autor/organizacja, data publikacji lub wersja, URL).
- Jeśli podano specyfikację/raport (np. 3GPP TR 38.843, TS 38.214):
  - Ustal dokładny numer, wersję i Release (np. Release 18, v18.0.0).
  - Instytucja: `3rd Generation Partnership Project ({3GPP})`.
- Jeśli podano artykuł/DOI:
  - Użyj wyszukiwarki lub odpytaj serwis (np. CrossRef/IEEE/arXiv), by pozyskać oficjalny wpis BibTeX.

### Krok 2: Odczytanie bieżących referencji

Przed edycją przeczytaj [references.bib](file:///home/finch/repo/praca-koncowa-zieba/praca/references.bib) za pomocą `view_file`:
- Sprawdź istniejące klucze cytowań pod kątem unikalności.
- Sprawdź styl formatowania w pliku.

### Krok 3: Przygotowanie wpisu BibTeX

Zastosuj zasady:
- Tytuły zawierające akronimy zabezpieczaj klamrami `{...}`, np. `{Massive {MIMO}}`, `{5G NR}`, `{{DeepMIMO}}`.
- Nazwy instytucji jako autorów/organizacji zabezpieczaj podwójnymi klamrami, np. `author = {{3GPP}}`.
- Pola `url` oraz `note = {Dostęp: RRRR-MM-DD}` dla źródeł online.

#### Przykłady wzorcowe:

**Specyfikacja / Raport 3GPP:**
```bibtex
@techreport{3gpp_tr38843,
  title        = {{Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR air interface}},
  author       = {{3GPP}},
  institution  = {3rd Generation Partnership Project ({3GPP})},
  type         = {Technical Report (TR)},
  number       = {38.843},
  version      = {18.0.0},
  year         = {2024},
  note         = {Release 18. Dostępny: \url{https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3983}}
}
```

**Strona internetowa / Portal techniczny:**
```bibtex
@online{sharetechnote_massive_mimo,
  author       = {Jaekyun Park},
  title        = {{5G | Massive MIMO - Definition}},
  journal      = {ShareTechNote},
  year         = {2024},
  url          = {https://www.sharetechnote.com/html/5G/5G_MassiveMIMO_Definition.html},
  note         = {Dostęp: 2026-10-06}
}
```

**Artykuł naukowy / Konferencja:**
```bibtex
@inproceedings{Alkhateeb2019,
  author    = {Alkhateeb, A.},
  title     = {{DeepMIMO}: A Generic Deep Learning Dataset for Millimeter Wave and Massive {MIMO} Applications},
  booktitle = {Proc. of Information Theory and Applications Workshop (ITA)},
  year      = {2019},
  pages     = {1--8},
  address   = {San Diego, CA}
}
```

### Krok 4: Zapisanie do pliku `praca/references.bib`

- Użyj `replace_file_content` lub edycji pliku, aby dopisać nowy wpis na końcu pliku.
- Upewnij się, że wpisy są oddzielone pojedynczą pustą linią.

### Krok 5: Instrukcja dla użytkownika dotycząca wstawienia do dokumentu

W odpowiedzi dla użytkownika przedstaw zwięźle:
1. **Podsumowanie wpisu** (klucz, typ, autorzy, tytuł).
2. **Sposób wstawienia w plikach Markdown (`praca/chapters/*.md`):**
   - W nawiasie kwadratowym na końcu zdania: `...tekst zdania [@klucz].`
   - Wielokrotne cytowanie: `...tekst [@klucz1; @klucz2].`
   - Cytowanie z numerem strony/rozdziału: `[@klucz, s. 15-20]`
   - Cytowanie w narracji: `@klucz wykazał, że...`
3. **Sposób wstawienia w czystym LaTeX (jeśli ma zastosowanie):**
   - `\cite{klucz}` lub `\citep{klucz}`
4. **Konkretny przykład zdania** dopasowany do kontekstu pracy i dodanego źródła.
