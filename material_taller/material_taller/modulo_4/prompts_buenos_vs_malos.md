# Prompts buenos vs. malos — IA aplicada a pipelines Kedro

Cuatro casos típicos de la sección 4.2, adaptados a lo que vas a pedirle a un
asistente de IA cuando trabajas dentro de un proyecto Kedro.

## Caso 1 — Agregar un nodo nuevo

**Malo:**
> "Hazme un nodo que procese los shuttles."

No dice qué transformación aplicar, ni el contrato de inputs/outputs que
Kedro necesita para conectar el nodo al resto del pipeline.

**Bueno:**
> "En `src/spaceflights/pipelines/data_processing/nodes.py` tengo
> `preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame`. Agrega una
> función `preprocess_reviews` con la misma firma que reciba el DataFrame de
> `reviews` y elimine las filas donde `review_scores_rating` sea nulo.
> Debe poder registrarse como nodo con `inputs='reviews'` y
> `outputs='preprocessed_reviews'`."

Da la firma esperada, el contrato de entrada/salida y la regla de negocio
exacta — todo lo que Kedro necesita para que el nodo encaje en el pipeline.

## Caso 2 — Debuggear un error de pipeline

**Malo:**
> "Mi pipeline no corre, ayuda."

**Bueno:**
> "Al correr `kedro run` me sale:
> `DatasetError: Failed while loading data from dataset CSVDataset(filepath=...).`
> `[Errno 2] No such file or directory: 'data/01_raw/companies.csv'`.
> Mi `catalog.yml` tiene la entrada `companies` apuntando a esa ruta. ¿Qué
> puede estar pasando y cómo lo verifico?"

Pega el mensaje de error completo y el fragmento relevante del `catalog.yml`
— sin eso, cualquier sugerencia es una adivinanza.

## Caso 3 — Refactorizar un nodo

**Malo:**
> "Mejora este código." *(pega 40 líneas sin contexto)*

**Bueno:**
> "Este nodo `create_model_input_table` hace dos merges seguidos y funciona,
> pero quiero que sea más legible. No cambies la lógica ni la firma
> (Kedro depende de que los nombres de parámetros coincidan con el
> `catalog.yml`), solo mejora nombres de variables intermedias y agrega un
> docstring corto."

Fija explícitamente qué NO debe cambiar — la firma de un nodo es un contrato
con el resto del pipeline, no un detalle de implementación.

## Caso 4 — Agregar manejo de errores

**Malo:**
> "Agrégale manejo de errores a mi nodo de entrenamiento."

**Bueno:**
> "En `train_model(X_train, y_train)` quiero que, si `X_train` llega vacío
> (0 filas), se levante un `ValueError` con un mensaje claro en vez de que
> falle dentro de `LinearRegression().fit()` con un traceback críptico. No
> agregues manejo para otros casos que no he pedido."

Un nodo Kedro que en la práctica devuelve `None` silenciosamente en vez de
fallar rompe el pipeline más adelante de forma difícil de rastrear — pide
errores explícitos, no silenciados.
