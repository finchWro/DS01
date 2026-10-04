---
name: praca-koncowa-verifier
description: >-
  Use this skill to verify the user's project, code, repository structure, and analytical
  methodology against the official graduation project requirements (Praca koncowa -
  Wymagania, kryteria oceny i katalog 40 tematow projektow, Studia Podyplomowe Data Science,
  Politechnika Wroclawska). Supports checking paragraphs 1, 2, 3, 4, 5, 6, 7, 10, and Zalacznik B.
---

# Praca Końcowa Verifier Skill

Ta umiejętność służy do audytu i weryfikacji zgodności projektu dyplomowego z oficjalnymi wymaganiami kierunku *Data Science - Analiza danych od podstaw* (Politechnika Wrocławska) opisanymi w dokumencie `docs/Praca_koncowa_wymagania_i_40_tematow.pdf`.

Obsługiwane paragrafy i sekcje wymagań:
- **1**: Cel i charakter pracy końcowej (reprodukowalność, poprawność procesu, wartość wyników negatywnych)
- **2**: Zasady ogólne (samodzielność, status prawny danych, publiczny/prywatny dostęp)
- **3**: Struktura i objętość pracy pisemnej (10 obowiązkowych rozdziałów, formatowanie, tabele i rysunki)
- **4**: Wymagania merytoryczne według poziomu (podstawowy, średni, zaawansowany - pipeline, split, baseline)
- **5**: Wymagania dotyczące kodu i repozytorium (5.1 Git, 5.2 Struktura katalogów, 5.3 Jakość i reprodukowalność)
- **6**: Błędy dyskwalifikujące (data leakage, błędny split czasowy/grupowy, accuracy na niezbalansowanych, itp.)
- **7**: Kryteria oceny pracy (100 pkt - rubryka oceniania)
- **10**: Etyka, dane osobowe, licencje i narzędzia AI (oświadczenie AI, zakaz danych osobowych, licencje)
- **Załącznik B**: Wzorcowa struktura repozytorium (pliki, katalogi, konwencje nazewnicze)

Szczegółowy wyciąg z wymagań znajduje się w:
[requirements_summary.md](./references/requirements_summary.md).

---

## Procedura weryfikacji

### Krok 1: Zapytaj użytkownika o zakres weryfikacji

Zawsze zapytaj użytkownika (np. przy użyciu narzędzia `ask_question`), które sekcje wymagań mają zostać uwzględnione w weryfikacji:

1. **Wszystkie wymagania (Pełny audyt)**: Sekcje 1, 2, 3, 4, 5, 6, 7, 10 oraz Załącznik B.
2. **Sekcja 5 + Załącznik B**: Weryfikacja kodu i struktury repozytorium (katalogi, pliki, notebooki, moduły, `.gitignore`).
3. **Sekcja 6**: Szybka weryfikacja pod kątem błędów krytycznych / dyskwalifikujących (wyciek danych, błędny podział, overfitting).
4. **Sekcja 4**: Weryfikacja merytoryczna wg poziomu trudności (podstawowy, średni lub zaawansowany).
5. **Sekcja 3 + 7 + 10**: Weryfikacja struktury tekstu pracy, etyki, licencji i oświadczenia AI.
6. **Wybór niestandardowy**: Użytkownik wskazuje konkretne paragrafy (np. 1, 5, 6).

Jeśli użytkownik w swoim zapytaniu już wskazał konkretne paragrafy, potwierdź wybór i przejdź bezpośrednio do weryfikacji.

---

### Krok 2: Pobranie stanu projektu

Przed ewaluacją zbadaj aktualny stan repozytorium:
1. Przejrzyj strukturę plików w projekcie (`list_dir`, ewentualnie `git status`).
2. Sprawdź obecność i zawartość kluczowych plików:
   - `README.md`
   - `requirements.txt` / `environment.yml`
   - `config.yaml`
   - `.gitignore` (w głównym katalogu i w `data/`)
   - `notebooks/` (nazwy i kolejność)
   - `src/` (moduły)
   - `outputs/`
   - `praca/`
3. Sprawdź kod w notebookach i modułach pod kątem:
   - Ziarna losowego (`seed` / `random_state`)
   - Podziału danych przed preprocessingiem
   - Obecności pipeline'ów i modeli bazowych (baseline)
   - Wycieków danych (data leakage) i chronologii w szeregach czasowych

---

### Krok 3: Analiza i raport niezgodności

Dla każdej wybranej przez użytkownika sekcji sporządź raport zawierający:
- **Status zgodności**:
  - `[ZGODNE]` – wymaganie spełnione
  - `[OSTRZEŻENIE]` – potencjalne ryzyko lub brak pełnej realizacji
  - `[BŁĄD / DYSKWALIFIKACJA]` – niespełnione wymaganie formalne lub wystąpienie błędu dyskwalifikującego
  - `[DO WERYFIKACJI]` – wymaga potwierdzenia przez autora (np. treść dokumentu docx)
- **Konkretne odniesienie do pliku / linii**: Z linkiem markdown (np. `[features.py](file:///path/to/features.py#L10)`)
- **Rekomendacja naprawcza**: Dokładny opis, co należy zmienić, aby praca spełniała kryteria.
