"""Solución del reto principal del Módulo 2 (sección 2.12).

Reto: agregar una columna derivada `price_per_passenger` a model_input_table
y una métrica adicional (MAE) al evaluate_model.

Esta es SOLO la parte que cambia respecto al material base de modulo_2/.
No reemplaza los archivos originales — muestra el diff conceptual.
"""

import logging

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# --- cambio en create_model_input_table (nodes_data_processing.py) ---
def create_model_input_table_con_derivada(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    rated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")
    rated_shuttles = rated_shuttles.drop("id", axis=1)
    model_input_table = rated_shuttles.merge(
        companies, left_on="company_id", right_on="id"
    )
    model_input_table = model_input_table.dropna()

    # Columna derivada pedida por el reto: precio por pasajero
    model_input_table["price_per_passenger"] = (
        model_input_table["price"] / model_input_table["passenger_capacity"]
    )
    return model_input_table


# --- cambio en evaluate_model (nodes_data_science.py) ---
def evaluate_model_con_mae(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    y_pred = regressor.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    logger = logging.getLogger(__name__)
    logger.info("R2 en datos de prueba: %.3f", r2)
    logger.info("MAE en datos de prueba: %.3f", mae)
