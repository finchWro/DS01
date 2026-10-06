# Zasady językowe i komunikacji w repozytorium

## Język projektu: Język polski (Polish)

W całym repozytorium oraz w interakcjach z agentami AI obowiązuje **język polski**:

1. **Komunikacja agenta z użytkownikiem**:
   - Wszystkie odpowiedzi, plany działań, pytania, komunikaty o błędach i podsumowania muszą być formułowane w języku polskim.

2. **Polska struktura repozytorium i nazwy plików**:
   - Notebooki analityczne w `notebooks/` muszą mieć polskie nazwy i prefiks numeryczny:
     - `00_pozyskanie_danych.ipynb`
     - `01_eda.ipynb`
     - `02_przygotowanie_danych.ipynb`
     - `03_modelowanie.ipynb`
     - `04_wyniki_i_wykresy.ipynb`
   - Moduły pomocnicze w `src/` muszą stosować polskie nazwy:
     - `wczytywanie_danych.py` (ładowanie i walidacja)
     - `inzynieria_cech.py` (transformacje i cechy)
     - `modele.py` (definicje estymatorów i pipeline'y)
     - `ewaluacja.py` (metryki, wykresy i walidacja)
   - Rozdziały pracy w `praca/chapters/`:
     - `01_tytulowa.md`, `02_streszczenie.md`, `03_wstep.md`, `04_dane.md`, `05_metodyka.md`, `06_wyniki.md`, `07_dyskusja.md`, `08_wnioski.md`, `09_zalaczniki_i_ai.md`

3. **Dokumentacja i praca pisemna**:
   - Wszystkie rozdziały pracy w `praca/chapters/*.md` oraz docelowy plik `praca/praca_koncowa.docx` muszą być pisane w języku polskim.
   - Wszystkie pliki `README.md` (w katalogu głównym, `praca/`, `data/`) muszą być zredagowane po polsku.

4. **Kod źródłowy, komentarze i docstringi**:
   - Komentarze w kodzie Pythona (`src/`, `notebooks/`) oraz docstringi modułów, klas i funkcji muszą być pisane w języku polskim.
   - Identyfikatory w kodzie powinny zachować spójność z polską terminologią dziedzinową lub przyjętym standardem bibliotek ML.

5. **Wykresy i wizualizacje (`outputs/figures/`)**:
   - Tytuły wykresów, etykiety osi X i Y, legendy oraz wszelkie adnotacje graficzne muszą być w języku polskim.

6. **Wiadomości zatwierdzeń (Git commit messages)**:
   - Wiadomości commitów muszą być formułowane w języku polskim (np. `feat: dodanie wstępnego czyszczenia danych w 02_przygotowanie_danych.ipynb`).
