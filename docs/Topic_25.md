# Topic 25: Prognozowanie generacji ze źródeł odnawialnych w Krajowym Systemie Elektroenergetycznym

**Poziom**: Zaawansowany | **Obszar**: IoT i energetyka  
**Źródło**: `docs/Praca_koncowa_wymagania_i_40_tematow.pdf` (strona 21–22) oraz `docs/Karta Wyboru Tematu 25 - OZE KSE.pdf`

---

## 1. Zadanie główne

Połączyć dane o generacji wiatrowej i fotowoltaicznej z danymi meteorologicznymi z niezależnego źródła i zbudować prognozę krótkoterminową wraz z oceną niepewności.

---

## 2. Zbiory danych i źródła (API)

### 2.1. API raportów PSE (Polskie Sieci Elektroenergetyczne)
- **Dostęp**: bez klucza, format JSON z filtrowaniem w składni OData.
- **Endpointy**:
  - Generacja (m.in. pola wiatrowe i fotowoltaiczne):  
    `https://api.raporty.pse.pl/api/his-wlk-cal`
  - Rynkowa cena energii (rozdzielczość 15 minut):  
    `https://api.raporty.pse.pl/api/rce-pln`
  - Zapotrzebowanie KSE (obciążenie KSE):  
    `https://api.raporty.pse.pl/api/obciazenie` lub `https://api.raporty.pse.pl/api/prog-obc`

### 2.2. API IMGW (Instytut Meteorologii i Gospodarki Wodnej)
- **Dostęp**: dane synoptyczne bez klucza.
- **Endpoint**:  
  `https://danepubliczne.imgw.pl/api/data/synop`
- **Archiwa meteorologiczne**:  
  `https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/`

---

## 3. Metody i narzędzia

- **Integracja danych**: integracja wielu źródeł o różnej rozdzielczości czasowej, uzgodnienie znaczników czasu i stref czasowych.
- **Inżynieria cech**: cechy meteorologiczne i kalendarzowe.
- **Modelowanie**: Gradient Boosting (np. LightGBM, XGBoost).
- **Walidacja**: walidacja kroczącym oknem (brak losowego podziału szeregu czasowego).
- **Ocena niepewności**: prognoza kwantylowa (przedziały niepewności).

---

## 4. Oczekiwany rezultat

Prognoza z przedziałami niepewności oraz analiza, ile faktycznie wnoszą dane meteorologiczne w porównaniu z modelem opartym wyłącznie na historii generacji (autoregresyjnym punktem odniesienia).

---

## 5. Uwagi i wymagania formalne

- **Wymagana atrybucja źródła danych**:  
  > *"Źródłem pochodzenia danych jest Instytut Meteorologii i Gospodarki Wodnej - Państwowy Instytut Badawczy"*.
- **Główny udział pracy**: największy udział pracy stanowi integracja i synchronizacja wieloźródłowych danych.
- **Poziom zaawansowany**: wymaga przeprowadzenia rzetelnego eksperymentu generalizacji, oceny stabilności/wrażliwości lub porównania z rzetelnym punktem odniesienia (baseline).
