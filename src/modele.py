"""Moduł odpowiedzialny za definicje modeli i potoków przetwarzania (Pipelines)."""

from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression


def utworz_baseline(losowe_ziarno: int = 42) -> Pipeline:
    """Tworzy model bazowy (punkt odniesienia) typu DummyClassifier."""
    return Pipeline([
        ("klasyfikator", DummyClassifier(strategy="most_frequent", random_state=losowe_ziarno))
    ])


def utworz_model_logistyczny(losowe_ziarno: int = 42) -> Pipeline:
    """Tworzy przykładowy potok regresji logistycznej."""
    return Pipeline([
        ("klasyfikator", LogisticRegression(random_state=losowe_ziarno, max_iter=1000))
    ])
