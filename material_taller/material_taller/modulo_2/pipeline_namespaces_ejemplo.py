"""Referencia — pipelines modulares con namespace (sección 2.9).

Ejemplo ilustrativo: dos instancias del pipeline de ciencia de datos
("activo" y "candidato"), cada una con su propio archivo de parámetros,
compartiendo el mismo model_input_table de entrada.

No es parte del pipeline base del taller — es una variante opcional para
quien quiera comparar dos configuraciones de modelo sin duplicar nodes.py.
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model

base_data_science = pipeline(
    [
        node(
            func=split_data,
            inputs=["model_input_table", "params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="regressor",
            name="train_model_node",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor", "X_test", "y_test"],
            outputs=None,
            name="evaluate_model_node",
        ),
    ]
)


def create_pipeline(**kwargs) -> Pipeline:
    activo = pipeline(
        base_data_science,
        namespace="activo",
        parameters={"params:model_options": "params:model_options_activo"},
        inputs={"model_input_table"},
    )
    candidato = pipeline(
        base_data_science,
        namespace="candidato",
        parameters={"params:model_options": "params:model_options_candidato"},
        inputs={"model_input_table"},
    )
    return activo + candidato
