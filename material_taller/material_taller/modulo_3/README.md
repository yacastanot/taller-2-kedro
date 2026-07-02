# Material complementario — Módulo 3

Archivos de referencia para calidad, versionado y empaquetado.

## Qué hay adentro

`test_data_science_pipeline.py` es el test de referencia de las secciones 3.2
y 3.3: un test unitario de `split_data` (incluyendo un caso negativo) y un test
de integración que corre el pipeline completo de ciencia de datos con
`SequentialRunner` y un `DataCatalog` en memoria.

`gitignore_template.txt` es la variante del `.gitignore` para un proyecto
Kedro (sección 3.4) — distinta a la del Taller 1 porque aquí además hay que
ignorar las capas de `data/` y `conf/local/`.

`README_template.md` es la plantilla del README de tu proyecto Kedro
(sección 3.5). Cópialo a la raíz de tu proyecto, renómbralo a `README.md` y
reemplaza `[Tu Nombre]`.

## La idea no es copiar

Escribe el test tú mismo siguiendo la guía; usa este archivo para comparar si
tu test no pasa. El `.gitignore` y el `README_template.md` sí están pensados
para copiarse literalmente — son plantillas, igual que en el Módulo 3 del
Taller 1.

## Cómo ejecutar los tests

```powershell
.venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

`pytest`, `pytest-cov` y `pytest-mock` no están en `requirements.txt` — son
dependencias de desarrollo declaradas en el grupo `dev` de `pyproject.toml`,
y `pip install -e ".[dev]"` las instala junto con tu proyecto en modo
editable en un solo paso. Si instalas `pytest` solo (sin `pytest-cov`),
`pytest` va a fallar con `unrecognized arguments: --cov-report --cov` porque
el starter ya trae la cobertura configurada por defecto en `pyproject.toml`.

Si `pytest` no encuentra tus pipelines, confirma que instalaste tu proyecto en
modo editable — sin eso, `from spaceflights.pipelines...` no resuelve.

## Empaquetar el proyecto (sección 3.6)

```powershell
kedro package
```

Esto genera un `.whl` en `dist/` que se puede instalar en otra máquina con
`pip install nombre_del_archivo.whl` y correr con `kedro run` — sin necesitar
el código fuente completo.

## Si algo falla

Sección 3.8 de la guía (Troubleshooting del Módulo 3).
