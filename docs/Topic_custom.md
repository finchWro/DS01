# Załącznik C. Karta wyboru tematu pracy końcowej

| Pole | Wartość |
| :--- | :--- |
| **Imię i nazwisko** | Błażej Zięba |
| **Numer wybranego tematu** | Zgłoszenie tematu własnego |
| **Tytuł tematu** | Maksymalizacja efektywności spektralnej (Spectral Efficiency) w sieciach 5G/6G Massive MIMO przy pomocy predykcji wiazki w dziedzinie przestrzeni. |
| **Poziom tematu** | zaawansowany |
| **Zbiór danych** | DeepMIMO Dataset (ASU): Znormalizowany zbiór wygenerowany silnikiem ray-tracingowym Remcom Wireless InSite dla scenariuszy 3GPP 5G NR / 6G outdoor (np. O1_28 GHz lub O1_60 GHz). Zawiera macierze kanału, kąty AoA/AoD, poziomy mocy i pozycje UE. |
| **Czy zbiór jest już pobrany i wczytany?** | tak |
| **Krótkie uzasadnienie wyboru (2-3 zdania)** | Temat wpisuje się w kierunek badań realizowanych w ramach AI-RAN w Nokii. Efektywność widmowa jest kluczowym parametrem definiującym wydajność sieci i pozwala poprawić ROI (Return on Investment – zwrot z inwestycji) operatorów. Wyższa efektywność widmowa oznacza optymalne wykorzystanie zasobu radiowego, który operatorzy nabywają na państwowych aukcjach częstotliwości, co przekłada się na niższe koszty i większe możliwości w świadczeniu usług. Predykcja wiązki w dziedzinie przestrzennej (spatial-domain Beam Prediction) jest jednym z kluczowych scenariuszy użycia AI/ML w stacji bazowej, rozważanych przez organizację standaryzacyjną 3GPP. Zastosowanie głębokich sieci neuronowych pozwala zastąpić wyczerpujące przeszukiwanie siatki wiązek modelowaniem predykcyjnym, skracając czas procedury wyboru o ponad 80% przy zachowaniu minimum 95% teoretycznej efektywności widmowej Shannona. Praca realizuje zaawansowany eksperyment walidacji przestrzennej (GroupKFold na strefach geograficznych), uniemożliwiający wyciek informacji o pozycji użytkownika.

Literatura: 

1. DeepMIMO: A Generic Deep Learning Dataset for Millimeter Wave and Massive MIMO Applications https://arxiv.org/html/1902.06435
2. 3GPP TR 38.843: Study on Artificial Intelligence (AI)/Machine Learning (ML) 
for NR air interface (Release 19) https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3983


|
| **Środowisko pracy (lokalne / Google Colab / inne)** | hybrydowe (lokalne / Google Colab z akceleracją GPU, Python 3.11, PyTorch / TensorFlow, DeepMIMO API, scikit-learn) |
| **Temat własny - jeśli tak, opis problemu, źródło danych i podstawa prawna ich wykorzystania** | **Opis problemu**: Budowa i ewaluacja modelu ML do szybkiej estymacji wiązki lub odpowiedzi kanału (CSI) dla użytkowników mobilnych w pasmach mmWave/sub-6GHz na podstawie pozycji przestrzennej oraz skróconych sygnałów pilotujących.<br>**Punkt odniesienia**: Exhaustive Beam Search (pełny skan radiowy).<br>**Źródło danych i licencja**: DeepMIMO Official Repository (Arizona State University). Licencja: Open Research Dataset (wymagane cytowanie oficjalnej publikacji naukowej DeepMIMO). |
| **Data i podpis uczestnika** | Błażej Zięba |
| **Decyzja kierownika studiów** | Temat zatwierdzono do realizacji (dr inż. Natalia Piórkowska) |
