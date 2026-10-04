# Wymagania formalne i merytoryczne pracy końcowej
Na podstawie dokumentu: *Praca końcowa - Wymagania, kryteria oceny i katalog 40 tematów projektów*
Studia podyplomowe „Data Science - Analiza danych od podstaw”, Wydział Informatyki i Telekomunikacji, Politechnika Wrocławska.

---

## 1. Cel i charakter pracy końcowej
- **Charakter pracy**: Samodzielny projekt analityczny rozwiązujący jasno zdefiniowany problem na rzeczywistym zbiorze danych przy użyciu narzędzi i metod poznanych w trakcie dwóch semestrów (przewidziano 16 godzin pracy własnej).
- **Cel nadrzędny**: Wykazanie umiejętności przeprowadzenia kompletnego, poprawnego metodologicznie i reprodukowalnego procesu analitycznego (od sformułowania pytania badawczego, przygotowania danych, budowy modelu, aż po krytyczną ocenę wyników i wskazanie ograniczeń).
- **Podejście do metryk**: Celem nie jest ślepe maksymalizowanie metryki kosztem metodologii. Poprawny proces z umiarkowaną jakością i uczciwymi wnioskami jest oceniany wyżej niż wysoka metryka uzyskana w wyniku błędu.
- **Zasada nadrzędna**: Wynik negatywny jest pełnoprawnym wynikiem („model nie przewyższył prostego punktu odniesienia, a oto dlaczego”), o ile został rzetelnie udokumentowany.

---

## 2. Zasady ogólne
- **Samodzielność**: Praca wykonywana wyłącznie indywidualnie. Brak możliwości prac zespołowych.
- **Wybór tematu**: Wybór tematu z katalogu (Część II) lub zatwierdzony temat własny (za pisemną zgodą kierownika studiów).
- **Prawa do danych**: Dane muszą być publicznie dostępne lub udostępnione przez kierownika studiów (Załącznik A). Dane objęte tajemnicą przedsiębiorstwa wymagają zgody właściciela i nie mogą trafić do publicznego repozytorium ani zewnętrznych narzędzi AI.

---

## 3. Struktura i objętość pracy
Orientacyjna objętość: 20–30 stron (poziom podstawowy i średni), do 35 stron (poziom zaawansowany). Czcionka 11 pkt, interlinia 1,15, marginesy 2,5 cm, numeracja stron, tabele i rysunki numerowane i podpisane.

Elementy składowe pracy:
1. **Strona tytułowa** (1 s.): Temat, imię i nazwisko, nazwa studiów, rok, nazwisko opiekuna.
2. **Streszczenie** (150–250 słów): Problem, dane, zastosowana metoda, główny wynik liczbowy, jeden wniosek.
3. **Wstęp** (2–3 s.): Kontekst, uzasadnienie wyboru, jasno postawiony cel i pytania badawcze (1 do 3), krótki przegląd literatury/rozwiązań.
4. **Charakterystyka zbioru danych** (3–5 s.): Źródło z pełnym odnośnikiem, licencja, sposób pozyskania, liczba obserwacji i zmiennych, tabela zmiennych z typami, statystyki opisowe, analiza braków i wartości odstających, znane ograniczenia zbioru.
5. **Metodyka** (4–6 s.): Obowiązkowy schemat (diagram) całego procesu, sposób przygotowania danych, uzasadnienie wyboru każdej metody, strategia podziału danych i walidacji, wybrane metryki wraz z uzasadnieniem wyboru, ustawienia zapewniające powtarzalność.
6. **Wyniki** (5–8 s.): Wyniki punktu odniesienia (baseline) i modeli, tabela porównawcza, min. 3 wykresy o rzeczywistej wartości informacyjnej, analiza istotności cech, analiza błędów modelu.
7. **Dyskusja i ograniczenia** (2–4 s.): Interpretacja wyników w kategoriach dziedziny, odniesienie do literatury, jawna lista ograniczeń pracy, wskazanie czego na podstawie tych danych stwierdzić nie można.
8. **Wnioski** (1–2 s.): Odpowiedzi na postawione we wstępie pytania badawcze oraz kierunki dalszych prac.
9. **Bibliografia**: Min. 8 pozycji w jednolitym stylu, obowiązkowo cytowanie źródła zbioru danych i ew. publikacji bazowej.
10. **Załączniki**: Odnośnik do repozytorium z kodem, ewentualne obszerne tabele i dodatkowe wykresy.

---

## 4. Wymagania merytoryczne według poziomu tematu
Wymagania są kumulatywne (średni = podstawowy + dodatki; zaawansowany = średni + dodatki):

- **Poziom Podstawowy**:
  - Kompletna eksploracyjna analiza danych (EDA) z wnioskami (nie tylko same wykresy).
  - Udokumentowane czyszczenie i przygotowanie danych.
  - Prosty punkt odniesienia (baseline: model naiwny lub reguła większościowa).
  - Co najmniej dwa modele właściwe.
  - Poprawny podział na zbiór treningowy i testowy wykonany PRZED jakimkolwiek przetwarzaniem.
  - Walidacja krzyżowa (CV).
  - Co najmniej 3 metryki wraz z uzasadnieniem ich doboru.
  - Interpretacja wyników w języku dziedziny.
- **Poziom Średni** (dodatkowo):
  - Całość przetwarzania zamknięta w obiekcie Pipeline (imputacja, skalowanie, kodowanie wyłącznie wewnątrz pipeline'u).
  - Świadome przeszukiwanie hiperparametrów z zagnieżdżoną lub rozdzielną walidacją.
  - Analiza istotności cech metodą odporną na współliniowość.
  - Systematyczna analiza błędów: gdzie i dla jakich obserwacji model zawodzi.
  - Uzasadniony wybór progu decyzyjnego lub metryki odzwierciedlającej koszt błędu.
- **Poziom Zaawansowany** (dodatkowo):
  - Jeden z elementów właściwy dla tematu: ocena kalibracji lub interpretowalność metodą SHAP, analiza stabilności/wrażliwości wyników na wybory analityczne, poprawnie przeprowadzony eksperyment generalizacji (nowe podmioty, nowy okres, nieznana klasa), ALBO model głęboki porównany z rzetelnym baseline'em wraz z jawną dyskusją kosztu obliczeniowego i wdrożenia.

---

## 5. Wymagania dotyczące kodu i repozytorium
- **5.1. Repozytorium**:
  - Przekazywane w repozytorium Git (GitHub / GitLab).
  - Historia commitów musi odzwierciedlać przebieg pracy (zakaz pojedynczego commita „praca końcowa”).
  - Całkowity zakaz umieszczania danych osobowych, danych pacjentów lub tajemnicy przedsiębiorstwa (także w historii commitów, outputach notebooków i plikach wynikowych).
- **5.2. Wymagana struktura**:
  - Repozytorium zgodne z Załącznikiem B.
  - `README.md` (opis, źródło danych, licencja, instrukcja odtworzenia krok po kroku, spis rezultatów).
  - `requirements.txt` lub `environment.yml` ze ściśle przypiętymi wersjami.
  - `data/` z plikiem `.gitignore` (danych nie commituje się; instrukcja pozyskania w README).
  - `notebooks/` numerowane w kolejności wykonania (`00_pozyskanie_danych`, `01_eda`, `02_przygotowanie`, `03_modele`, `04_wyniki`).
  - `src/` funkcje wielokrotnie używane przeniesione do modułów.
  - `outputs/` generowane wykresy, tabele i zapisane modele.
- **5.3. Reprodukowalność i jakość**:
  - Ustawione stałe ziarno generatora losowego (`random_seed`) we wszystkich miejscach z losowością.
  - Uruchomienie notebooków w kolejności na czystym środowisku musi odtworzyć wszystkie liczby i wykresy z tekstu pracy.
  - Komórki notebooków wykonane w kolejności rosnącej, bez błędów w outputach.
  - Brak zakomentowanego martwego kodu, brak ścieżek absolutnych (np. `C:\Users\...`), brak powtórzeń kodu metodą kopiuj-wklej.
  - Czytelne nazwy zmiennych i funkcji; komentarze wyjaśniające „dlaczego”, a nie „co”.

---

## 6. Błędy dyskwalifikujące
Błędy unieważniające wynik i uniemożliwiające dopuszczenie do obrony:
1. **Skalowanie lub imputacja przed podziałem danych**: Przenosi informację ze zbioru testowego do treningowego.
2. **Selekcja cech na całym zbiorze**: Wybór cech powiązanych ze zmienną celu przed podziałem na zbiory (fałszuje wyniki o kilkanaście p.p.).
3. **Ocena modelu na danych, na których był uczony**: Testowanie na zbiorze treningowym (mierzy pamięć, nie generalizację).
4. **Losowy podział szeregu czasowego**: W zadaniach prognostycznych podział musi być ściśle chronologiczny.
5. **Losowy podział danych zawierających wiele obserwacji tego samego podmiotu**: Wymagany podział grupowy (`GroupKFold`), by obserwacje tego samego podmiotu nie trafiły do obu zbiorów.
6. **Wyciek zmiennej celu**: Obecność cech powstających po zdarzeniu lub zawierających bezpośrednią informację o celu.
7. **Trafność (accuracy) jako jedyna metryka przy klasach niezbalansowanych**: Niezdatna przy asymetrii klas (model stały może mieć np. 99% accuracy).
8. **Wielokrotne dobieranie modelu na zbiorze testowym**: Zbiór testowy użyty do optymalizacji przestaje być testowy (do doboru służy zbiór walidacyjny / CV).
9. **Wnioski przyczynowe z danych obserwacyjnych**: Mylenie korelacji lub ważności cech ze związkiem przyczynowo-skutkowym.

---

## 7. Kryteria oceny pracy (skala 100 pkt)
1. **Sformułowanie problemu i celu (10 pkt)**: Konkretne i sprawdzalne pytania badawcze, merytoryczne uzasadnienie tematu.
2. **Praca ze zbiorem danych (20 pkt)**: Rzetelność EDA, udokumentowane czyszczenie, świadomość ograniczeń, uzasadnienie braków i odstających.
3. **Metodyka i poprawność walidacji (25 pkt - NAJWYŻSZA WAGA)**: Poprawność walidacji, brak wycieku informacji (data leakage), uzasadnienie metod i metryk, obecność baseline.
4. **Wyniki i ich interpretacja (15 pkt)**: Odpowiedź na pytania badawcze, jakość wykresów, analiza błędów, uczciwość ograniczeń.
5. **Jakość i reprodukowalność kodu (15 pkt)**: Struktura repozytorium, odtwarzalność wyników, czystość kodu, zgodność liczb z pracą.
6. **Jakość redakcyjna i bibliografia (10 pkt)**: Kompletność struktury, język, jednolitość min. 8 cytowań, opis tabel i rysunków.
7. **Samodzielność i inicjatywa (5 pkt)**: Dodatkowy eksperyment, własna weryfikacja, literatura pierwotna.

Skala ocen: 90–100: 5.0 | 80–89: 4.5 | 70–79: 4.0 | 60–69: 3.5 | 50–59: 3.0 | <50: 2.0 (niedostateczna).

---

## 10. Etyka, dane osobowe, licencje i narzędzia AI
- **10.1. Dane i licencje**: Każdy zbiór zacytowany (nazwa, autor/instytucja, url, data pobrania, licencja, publikacja źródłowa). Respektowanie warunków licencji (np. non-commercial, atrybucja IMGW/GIOŚ). Zakaz danych osobowych i pacjentów.
- **10.2. Odpowiedzialność analityczna**: Obowiązkowa lista ograniczeń pracy. W tematach dotyczących ludzi omówienie asymetrii błędów i fairness. Jawne oznaczenie danych syntetycznych.
- **10.3. Narzędzia AI**:
  - *Dozwolone*: Pomoc w pisaniu i debugowaniu kodu, wyjaśnianie błędów, korekta językowa tekstu, poszukiwanie literatury (z weryfikacją).
  - *Niedozwolone*: Generowanie gotowego tekstu rozdziałów, generowanie wyników/liczb/wykresów bez uruchomienia własnego kodu, generowanie fałszywych referencji bibliograficznych.
  - *Wymagane*: Krótkie oświadczenie na końcu pracy o zakresie użycia AI. Zakaz wprowadzania do zewnętrznych narzędzi AI danych poufnych i udostępnionych przez kierownika.

---

## Załącznik B. Wzorcowa struktura repozytorium
Obowiązkowe nazwy katalogów i szablon zawartości:

```text
praca-koncowa-<nazwisko>/
├── README.md               # Opis, źródło danych, licencja, instrukcja odtworzenia krok po kroku
├── requirements.txt        # Zależności ze ściśle przypiętymi wersjami
├── .gitignore              # Obowiązkowo wyklucza katalog data/
├── config.yaml             # Parametry i ziarno generatora losowego (seed)
├── data/
│   ├── raw/                # Dane źródłowe (nie commitowane)
│   ├── processed/          # Dane po przetworzeniu (nie commitowane)
│   ├── README.md           # Skąd i jak pobrać dane
│   └── .gitignore          # Zabezpieczenie katalogu danych
├── notebooks/              # Numerowane wg kolejności wykonania
│   ├── 00_pozyskanie_danych.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_przygotowanie_danych.ipynb
│   ├── 03_modelowanie.ipynb
│   └── 04_wyniki_i_wykresy.ipynb
├── src/                    # Moduły z funkcjami pomocniczymi
│   ├── data_loader.py      # Wczytywanie i walidacja danych
│   ├── features.py         # Inżynieria cech
│   ├── models.py           # Definicje modeli i pipeline
│   └── evaluation.py       # Metryki i wykresy
├── outputs/                # Generowane przez kod
│   ├── figures/            # Wykresy użyte w pracy
│   ├── tables/             # Tabele wynikowe
│   └── models/             # Zapisane modele
└── praca/
    ├── praca_koncowa.docx  # Tekst pracy dyplomowej
    └── prezentacja.pptx    # Prezentacja na obronę
```
