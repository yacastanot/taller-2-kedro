# Material complementario — Módulo 2

Archivos de referencia para el Módulo 2: los dos pipelines del taller.

## Qué hay adentro

`nodes_data_processing.py` y `pipeline_data_processing.py` son la versión de
referencia del pipeline de procesamiento de datos (secciones 2.2 y 2.3):
`preprocess_companies`, `preprocess_shuttles` y `create_model_input_table`.

`nodes_data_science.py` y `pipeline_data_science.py` corresponden al pipeline de
ciencia de datos (sección 2.8): `split_data`, `train_model` y `evaluate_model`
con `LinearRegression`. `parameters_data_science.yml` es el archivo de
parámetros que acompaña a ese pipeline.

En `soluciones_retos/` está la solución del reto principal de la sección 2.12
(columna derivada `price_per_passenger` y métrica MAE adicional).

`catalog_factories_ejemplo.yml`, `pipeline_namespaces_ejemplo.py` y
`hooks_ejemplo.py` son material de las secciones 2.4, 2.9 y 2.10
(Dataset Factories, pipelines modulares con namespace, y Hooks). Ninguno de
los tres es obligatorio para que el taller funcione — son técnicas
adicionales para cuando un proyecto Kedro crece más allá de dos pipelines.

## La idea no es copiar

Cada archivo indica en su docstring en qué ruta del proyecto va
(`src/spaceflights/pipelines/<nombre>/nodes.py`, por ejemplo). La guía te pide
escribirlos tú mismo con `kedro pipeline create <nombre>` y editando esos
archivos paso a paso — usa esta carpeta para comparar, no para copiar y pegar
de una vez.

## Cómo ejecutarlo

Asumiendo que ya integraste ambos pipelines en tu proyecto:

```powershell
.venv\Scripts\activate
kedro run
```

Para correr solo uno de los dos pipelines:

```powershell
kedro run --pipeline=data_processing
kedro run --pipeline=data_science
```

Para ver el linaje completo:

```powershell
kedro viz run
```

## Si algo falla

Sección 2.13 de la guía (Troubleshooting del Módulo 2). El error más común es
un nombre de dataset que no coincide entre `catalog.yml` y los `inputs`/`outputs`
de un nodo — Kedro te dice exactamente cuál falta en el mensaje de error.
