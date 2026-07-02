"""Referencia de la sección 1.7 — cargar datos del catálogo sin correr un pipeline.

Ejecútalo desde la raíz de tu proyecto Kedro (donde está pyproject.toml) con:

    kedro run --pipeline=none   # no existe, esto es solo un ejemplo de bootstrap manual
    python modulo_1/explorar_catalogo.py

En la práctica casi nunca vas a escribir un script como este — para explorar
datos interactivamente se usa `kedro ipython` (sección 1.7 de la guía). Este
archivo existe solo para que veas qué hace `kedro ipython` por debajo: arranca
el proyecto y te deja un `catalog` ya cargado.
"""

from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

project_path = Path(__file__).resolve().parents[3]
bootstrap_project(project_path)

with KedroSession.create(project_path=project_path) as session:
    context = session.load_context()
    catalog = context.catalog

    print("Datasets registrados en el catálogo:")
    for nombre in catalog.list():
        print(f"  - {nombre}")

    companies = catalog.load("companies")
    print("\nPrimeras filas de companies:")
    print(companies.head())
