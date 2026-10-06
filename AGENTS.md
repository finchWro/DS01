# Zasady projektu i wytyczne dla agentów AI

W tym projekcie obowiązują następujące zasady:

## 1. Język projektu: Język polski
- Cała komunikacja z użytkownikiem, dokumentacja (`praca/chapters/`, pliki `README.md`), komentarze w kodzie, docstringi modułów oraz opisy i etykiety na wykresach (`outputs/figures/`) muszą być tworzone w **języku polskim**.
- Szczegółowe zasady opisano w [language.md](file:///home/finch/repo/DS01/.agents/rules/language.md).

## 2. Polska konwencja nazewnicza struktury repozytorium
- Wszystkie pliki dokumentacji, rozdziały pracy oraz notebooki analityczne i moduły pomocnicze muszą stosować **polskie nazwy** (zgodnie z Załącznikiem B do wytycznych):
  - **Notebooki (`notebooks/`)**:
    - `00_pozyskanie_danych.ipynb`
    - `01_eda.ipynb`
    - `02_przygotowanie_danych.ipynb`
    - `03_modelowanie.ipynb`
    - `04_wyniki_i_wykresy.ipynb`
  - **Moduły Pythona (`src/`)**:
    - `wczytywanie_danych.py` (lub `ladowanie_danych.py`)
    - `inzynieria_cech.py`
    - `modele.py`
    - `ewaluacja.py`
  - **Katalog pracy pisemnej (`praca/`)**:
    - `praca/chapters/`: polskie nazwy rozdziałów (`01_tytulowa.md`, `02_streszczenie.md`, `03_wstep.md`, `04_dane.md`, `05_metodyka.md`, `06_wyniki.md`, `07_dyskusja.md`, `08_wnioski.md`, `09_zalaczniki_i_ai.md`)
    - `praca/praca_koncowa.docx`
    - `praca/prezentacja.pptx`
  - **Dane (`data/`)**:
    - `data/raw/` (dane surowe) oraz `data/processed/` (dane przetworzone) zabezpieczone plikiem `.gitignore` przed dodaniem do repozytorium.
  - **Wyniki (`outputs/`)**:
    - `outputs/figures/` (wykresy z polskimi podpisami i osiami)
    - `outputs/tables/` (tabele wynikowe)
    - `outputs/models/` (zapisane modele i pipeline'y)

## 3. Standardy pracy końcowej Data Science
- Wszystkie zadania i analizy muszą spełniać wymagania formalne i metodyczne kierunku *Data Science* PWr:
  - Bezwzględny zakaz wycieków danych (*data leakage* – skalowanie i inżynieria cech wyłącznie po podziale danych i wewnątrz `Pipeline`).
  - Poprawny podział na zbiór treningowy/testowy (czasowy dla szeregów czasowych, `GroupKFold` dla powtarzających się podmiotów).
  - Obowiązkowy prosty punkt odniesienia (*baseline*).
  - Zapewnienie pełnej reprodukowalności (stały `random_state`/`seed` zdefiniowany centralnie w `config.yaml`).
