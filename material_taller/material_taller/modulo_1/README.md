# Material complementario — Módulo 1

Archivos de referencia para el Módulo 1 del taller de Kedro.

## Qué hay adentro

`catalog_ejemplo.yml` es el resultado esperado de la sección 1.6, donde registras
`companies`, `reviews` y `shuttles` en el Data Catalog. `explorar_catalogo.py` es un
ejemplo de lo que `kedro ipython` hace por debajo cuando arranca tu proyecto y te
deja el `catalog` disponible en la sesión — lo incluyo para que entiendas el
mecanismo, no porque vayas a usarlo tal cual.

## La idea no es copiar

El proyecto Kedro completo lo genera el comando `kedro new --starter spaceflights-pandas`
de la sección 1.3 — no lo vas a encontrar en esta carpeta. Estos archivos son solo
para comparar contra lo que tú mismo edites en `conf/base/catalog.yml` dentro de tu
propio proyecto.

Si algo no te carga, compara tu `catalog.yml` contra `catalog_ejemplo.yml` línea por
línea: los errores más comunes son indentación (YAML es sensible a espacios) y rutas
de archivo mal escritas.

## Cómo probarlo

Asumiendo que ya creaste el proyecto y activaste tu entorno virtual del Módulo 0:

```powershell
cd ruta\a\tu\proyecto\spaceflights
.venv\Scripts\activate
kedro ipython
```

Dentro de la sesión de IPython:

```python
companies = catalog.load("companies")
companies.head()
```

## Si algo falla

Consulta la sección 1.11 (Troubleshooting del Módulo 1) en la guía principal.
