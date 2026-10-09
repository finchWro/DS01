# 1. Wstęp

<!-- Wymagania formalne: 2–3 strony.
Elementy obowiązkowe:
- Kontekst biznesowy / naukowy oraz uzasadnienie wyboru tematu.
- Jasno sformułowany cel główny pracy.
- Od 1 do 3 konkretnych, weryfikowalnych pytań badawczych.
- Krótki przegląd literatury i dotychczasowych rozwiązań dziedzinowych.
-->

## 1.1. Kontekst i uzasadnienie tematu

Operatorzy telekomunikacyjni, ang. CSP (Communication Service Providers) działają na silnie konkurencyjnym rynku, który wymaga ciągłej redukcji kosztów. Największe nakłady inwestycyjne związane są z zakupem pasma na licytacjach krajowych. Efektywne wykorzystanie tego zasobu decyduje o przewadze konkurencyjnej na rynku usług telekomunikacyjnych. Miarą efektywności użycia pasma jest efektywność spektralna (ang. spectral efficiency), która definiowana jest jako ilość przesłanych bitów na sekundę przypadająca na jednostkę szerokości pasma. Zazwyczaj jest wyrażana w jednostkach bit/s/Hz. 

W celu poprawienia efektywności spektralnej operatorzy wykorzystują w sieciach komórkowych technologię Massive MIMO (ang. Multiple Input Multiple Output), która wykorzystuje macierze antenowe o liczbie elementów znacznie przekraczającej liczbę jednocześnie obsługiwanych użytkowników. Dzięki zwielokrotnieniu przestrzennemu (ang. spatial multiplexing) możliwa jest jednoczesna transmisja do wielu użytkowników w tym samym zasobie częstotliwościowym i czasowym, co bezpośrednio zwiększa efektywność spektralną systemu. [@sharetechnote_massive_mimo]

Aby dalej poprawić efektywność spektralną organizacja standaryzująca 3GPP przeprowadziła analizę możliwości wykorzystania uczenia maszynowego w telekomunikacji. W efekcie powstał raport techniczny TR 38.843 "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR air interface", w którym opisano scenariusz predykcji wiązki w przestrzeni przy wykorzystaniu modeli uczenia maszynowego. 

W pracy wykorzystano zbiór danych wygenerowany za pomocą frameworku DeepMIMO (Arizona State University), opartego na danych z symulacji ray-tracingowych przeprowadzonych w oprogramowaniu Remcom Wireless InSite dla scenariusza 3GPP 5G NR outdoor. [@Alkhateeb2019]

## 1.2. Cel pracy i pytania badawcze

Celem niniejszej pracy jest implementacja opisanego w raporcie TR 38.843 scenariusza predykcji wiązki w przestrzeni z wykorzystaniem bibliotek do uczenia maszynowego w języku Python oraz analiza uzyskanej efektywności spektralnej i porównanie jej z efektywnością spektralną uzyskaną przy wykorzystaniu tradycyjnych metod bazujących na pomiarach pilotowych.[@3gpp_tr38843]

W ramach pracy postawiono następujące pytania badawcze:
1. **PB1:** [Pierwsze pytanie badawcze...]
2. **PB2:** [Drugie pytanie badawcze...]
3. **PB3:** [Trzecie pytanie badawcze...]

## 1.3. Przegląd literatury

[Krótki przegląd stanu wiedzy wraz z cytowaniami, np. [@breiman2001random; @pedregosa2011scikit]...]

\newpage
