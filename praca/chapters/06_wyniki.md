# 4. Wyniki

<!-- Wymagania formalne: 5–8 stron.
Elementy obowiązkowe (§3, §4, §7):
- Tabela porównawcza wyników punktu odniesienia (baseline) i modeli właściwych na zbiorze walidacyjnym i testowym.
- Minimum 3 merytoryczne wykresy (np. krzywe ROC/PR, macierz pomyłek, krzywe uczenia, residual plots).
- Analiza istotności cech (feature importance odporna na współliniowość, np. permutation importance lub SHAP).
- Analiza błędów modelu: systematyczne zbadanie przypadków, w których model zawodzi (false positives / false negatives).
-->

## 4.1. Porównanie modeli z punktem odniesienia

Tabela 2. Zbiorcze zestawienie metryk na zbiorze testowym.

| Model | Metryka 1 (np. PR-AUC) | Metryka 2 (np. F1-score) | Metryka 3 (np. ROC-AUC) |
| :--- | :--- | :--- | :--- |
| **Baseline (Dummy)** | 0.150 | 0.000 | 0.500 |
| **Model 1 (Logistic Regression)** | 0.580 | 0.610 | 0.790 |
| **Model 2 (Random Forest)** | 0.670 | 0.690 | 0.850 |
| **Model 3 (XGBoost - finalny)** | **0.720** | **0.730** | **0.880** |

## 4.2. Wizualizacja jakości predykcji

Poniższe rysunki przedstawiają szczegółową ocenę zachowania najlepszego modelu:

![Rysunek 2. Krzywa Precision-Recall dla modeli na zbiorze testowym.](../outputs/figures/pr_curve.png)

![Rysunek 3. Znormalizowana macierz pomyłek modelu finalnego.](../outputs/figures/confusion_matrix.png)

## 4.3. Analiza ważności cech

W celu interpretacji wpływu poszczególnych cech na predykcje zastosowano metodę Permutation Importance / wartości SHAP:

![Rysunek 4. Istotność cech wyznaczona metodą Permutation Feature Importance.](../outputs/figures/feature_importance.png)

## 4.4. Analiza błędów (Error Analysis)

[Szczegółowa analiza przypadków fałszywie pozytywnych (FP) i fałszywie negatywnych (FN): jakie profile obserwacji sprawiają modelowi największą trudność i dlaczego...]

\newpage
