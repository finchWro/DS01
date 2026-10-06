"""Moduł ewaluacji modeli, wyznaczania metryk i generowania wykresów z polskimi etykietami."""

from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def oblicz_metryki(y_prawdziwe, y_predykcja) -> dict:
    """Zwraca słownik kluczowych metryk oceny modelu."""
    # Obliczenia metryk
    return {}


def zapisz_macierz_pomylek(y_prawdziwe, y_predykcja, sciezka_zapisu: Path | str, tytul: str = "Macierz pomyłek"):
    """Generuje i zapisuje macierz pomyłek z polskimi etykietami."""
    fig, ax = plt.subplots(figsize=(6, 5))
    cm = confusion_matrix(y_prawdziwe, y_predykcja)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(ax=ax, cmap="Blues")
    ax.set_title(tytul)
    ax.set_xlabel("Klasa przewidywana")
    ax.set_ylabel("Klasa rzeczywista")
    plt.tight_layout()
    plt.savefig(sciezka_zapisu, dpi=300)
    plt.close()
