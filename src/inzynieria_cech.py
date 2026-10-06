"""Moduł odpowiedzialny za transformacje i inżynierię cech."""

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class InzynieriaCech(BaseEstimator, TransformerMixin):
    """Przykładowy transformer cech zgodny ze scikit-learn Pipeline."""

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_kopia = X.copy()
        # Miejsce na transformacje i nowe cechy
        return X_kopia
