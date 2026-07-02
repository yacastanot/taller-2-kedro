# Solución del reto — Módulo 2

`reto_price_per_passenger.py` resuelve el reto de la sección 2.12: agregar la
columna derivada `price_per_passenger` a `model_input_table` y una métrica
adicional (MAE) al nodo `evaluate_model`.

No es un archivo para copiar y pegar completo — muestra únicamente las dos
funciones que cambian respecto al material base de `modulo_2/`, para que
compares el "antes" (`nodes_data_processing.py` / `nodes_data_science.py`) con
el "después". Tú tienes que integrar el cambio en tu propio proyecto:

1. Agrega las tres líneas de `price_per_passenger` dentro de tu
   `create_model_input_table`.
2. Agrega `mean_absolute_error` a los imports y a `evaluate_model` en tu
   proyecto.
3. Vuelve a correr `kedro run` y confirma en el log que aparecen tanto el R2
   como el MAE.
