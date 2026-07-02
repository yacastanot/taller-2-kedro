"""Referencia — nodos del pipeline de ciencia de datos (sección 2.7).

Va en src/spaceflights/pipelines/data_science/nodes.py dentro de tu proyecto.
"""

import logging

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """Separa los datos en conjuntos de entrenamiento y prueba."""
    X = data[parameters["features"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Entrena el modelo de regresión lineal."""
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series):
    """Calcula el R2 del modelo sobre el conjunto de prueba y lo deja en el log."""
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("El modelo tiene un coeficiente R2 de %.3f en datos de prueba.", score)
