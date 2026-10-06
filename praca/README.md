# Katalog Pracy Końcowej (`praca/`)

W tym katalogu znajduje się źródłowy tekst pracy końcowej pisany w formacie Markdown oraz mechanizm automatycznego generowania docelowego pliku `praca_koncowa.docx` wymaganego przez regulamin studiów.

---

## 1. Struktura katalogu

```text
praca/
├── chapters/               # Źródła rozdziałów w formacie Markdown
│   ├── 01_tytulowa.md      # Strona tytułowa
│   ├── 02_streszczenie.md  # Streszczenie (150–250 słów)
│   ├── 03_wstep.md         # Wstęp i pytania badawcze (2–3 s.)
│   ├── 04_dane.md          # Zbiór danych, źródło, licencja, EDA (3–5 s.)
│   ├── 05_metodyka.md      # Metodyka, diagram, pipeline, walidacja (4–6 s.)
│   ├── 06_wyniki.md        # Wyniki, baseline, wykresy, feature importance (5–8 s.)
│   ├── 07_dyskusja.md      # Interpretacja domenowa, ograniczenia (2–4 s.)
│   ├── 08_wnioski.md       # Odpowiedzi na pytania badawcze (1–2 s.)
│   └── 09_zalaczniki_i_ai.md # Link do repozytorium, oświadczenie AI, bibliografia
├── references.bib          # Baza cytowań BibTeX (min. 8 pozycji)
├── build.sh                # Skrypt bash do generowania DOCX przez Pandoc
├── Makefile                # Alternatywne uruchomienie przez polecenie `make`
├── reference.docx          # Opcjonalny szablon stylów Worda (czcionka 11pt, interlinia 1.15)
└── praca_koncowa.docx      # Wyjściowy plik pracy (wymagany Załącznikiem B)
```

---

## 2. Wymagania wstępne

Do generowania dokumentu Word potrzebne jest narzędzie **Pandoc**.

### Instalacja Pandoc:
* **Ubuntu / Debian:**
  ```bash
  sudo apt update && sudo apt install -y pandoc
  ```
* **Conda / Mamba:**
  ```bash
  conda install -c conda-forge pandoc
  ```

---

## 3. Generowanie dokumentu `praca_koncowa.docx`

Możesz uruchomić budowanie na dwa sposoby:

```bash
# Sposób 1: Skrypt Bash
chmod +x praca/build.sh
./praca/build.sh

# Sposób 2: Make
cd praca && make
```

Skrypt automatycznie:
1. Zbiera rozdziały z `chapters/` w kolejności numerycznej.
2. Formatuje tabele i wstawia rysunki z katalogu `outputs/figures/`.
3. Przetwarza cytowania z pliku `references.bib` za pomocą modułu `--citeproc`.
4. Tworzy automatyczny spis treści (TOC).
5. Zapisuje gotowy dokument `praca/praca_koncowa.docx`.

---

## 4. Własne formatowanie (czcionka 11 pt, interlinia 1.15, marginesy 2.5 cm)

Pandoc potrafi przejąć style z pliku wzorcowego:
1. Wygeneruj domyślny plik referencyjny:
   ```bash
   pandoc -o praca/reference.docx --print-default-data-file reference.docx
   ```
2. Otwórz `praca/reference.docx` w programie Microsoft Word lub LibreOffice Writer.
3. W menu stylów zmodyfikuj styl **Normalny / Podstawowy**:
   - Czcionka: **11 pkt** (np. Calibri, Arial lub Times New Roman),
   - Interlinia: **1,15**,
   - Marginesy strony: **2,5 cm**.
4. Zapisz plik pod nazwą `praca/reference.docx`.
5. Każde kolejne uruchomienie `./praca/build.sh` automatycznie zastosuje te formatowania do nowo wygenerowanego dokumentu.
