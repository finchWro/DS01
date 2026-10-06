# 3. Metodyka

<!-- Wymagania formalne: 4–6 stron.
Elementy obowiązkowe (§3, §4, §6):
- Obowiązkowy schemat blokowy / diagram całego procesu analitycznego.
- Czyszczenie i przygotowanie danych (zamknięte w Pipeline).
- Strategia podziału danych: trening / walidacja / test PRZED jakimkolwiek przetwarzaniem.
  * Uwaga na wycieki danych (data leakage)!
  * Dla szeregów czasowych: ściśle chronologiczny split (TimeSeriesSplit).
  * Dla powtarzających się jednostek: GroupKFold.
- Zestawienie metryk oceny z merytorycznym uzasadnieniem ich doboru (np. F1, ROC-AUC, PR-AUC).
- Zapewnienie pełnej reprodukowalności (stały random_seed / parametry w config.yaml).
-->

## 3.1. Schemat procesu analitycznego

Poniższy diagram przedstawia kompletny proces przetwarzania danych, modelowania i walidacji:

<!-- Możesz wstawić wygenerowany diagram z outputs/figures/flowchart.png -->
![Rysunek 1. Schemat blokowy procesu badawczo-analitycznego.](../outputs/figures/flowchart.png)

## 3.2. Podział danych i strategia walidacji

W celu uniknięcia wycieku danych (*data leakage*), podział na zbiór treningowy i testowy został wykonany jako pierwszy krok przed etapem preprocessingu:
- Podział: [np. 80% trening, 20% test z zachowaniem stratyfikacji / podziału czasowego].
- Walidacja krzyżowa: [np. 5-krotna stratyfikowana walidacja krzyżowa (StratifiedKFold)].

## 3.3. Przygotowanie danych i pipeline

Wszystkie transformacje (skalowanie, imputacja braków, kodowanie zmiennych kategorycznych) zostały zaimplementowane w ramach obiektów `Pipeline` biblioteki `scikit-learn`...

## 3.4. Dobór modeli i punkt odniesienia (Baseline)

- **Model bazowy (baseline):** [np. DummyClassifier - klasa większościowa / naiwny model średniej].
- **Modele kandydujące:** [np. Regresja Logistyczna, Random Forest, XGBoost / LightGBM].

## 3.5. Metryki ewaluacji

Uzasadnienie doboru metryk:
1. **[Metryka 1, np. PR-AUC / ROC-AUC]:** [Uzasadnienie merytoryczne i biznesowe]
2. **[Metryka 2, np. F1-score / Balanced Accuracy]:** [Uzasadnienie merytoryczne]
3. **[Metryka 3, np. Brier Score / Log-Loss]:** [Uzasadnienie oceny prawdopodobieństw]

\newpage
