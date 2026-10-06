"""Moduł odpowiedzialny za wczytywanie i wstępną walidację danych źródłowych."""

from pathlib import Path
import pandas as pd


def wczytaj_dane_surowe(sciezka_pliku: Path | str) -> pd.DataFrame:
    """Wczytuje zbiór danych ze ścieżki i przeprowadza podstawową walidację.

    Parametry:
        sciezka_pliku: Ścieżka do pliku z danymi (np. CSV, Parquet).

    Zwraca:
        pd.DataFrame: Wczytana ramka danych.
    """
    sciezka = Path(sciezka_pliku)
    if not sciezka.exists():
        raise FileNotFoundError(f"Nie odnaleziono pliku: {sciezka}")
    return pd.read_csv(sciezka)
