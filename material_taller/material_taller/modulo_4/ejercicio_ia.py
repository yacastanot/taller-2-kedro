"""Ejercicio práctico del Módulo 4 (sección 4.4) — punto de partida.

Este archivo NO va directo a tu proyecto Kedro. Es el enunciado de las cuatro
tareas que vas a resolver con apoyo de un asistente de IA, cada una tocando
una parte distinta de tu pipeline `spaceflights`. Ve tachando cada tarea a
medida que la completes en tu propio proyecto.

Antes de empezar, confirma que tu pipeline `data_processing` + `data_science`
corre sin errores con `kedro run` (Módulos 1 y 2). Vas a construir sobre eso.
"""

# ---------------------------------------------------------------------------
# TAREA 1 (fácil) — Agregar un nodo de preprocesamiento
#
# Pídele a tu asistente de IA una función `preprocess_reviews(reviews)` que
# elimine filas con `review_scores_rating` nulo, siguiendo el Caso 1 de
# prompts_buenos_vs_malos.md. Regístrala como nodo en el pipeline
# `data_processing` con inputs="reviews", outputs="preprocessed_reviews".
# No la conectes todavía a create_model_input_table — solo verifica con
# `kedro run --nodes=preprocess_reviews_node` que corre sola.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TAREA 2 (medio) — Debuggear un error real
#
# Rompe intencionalmente tu catalog.yml (cambia una ruta de archivo) y corre
# `kedro run`. Pega el traceback completo a tu asistente de IA usando el
# Caso 2 de prompts_buenos_vs_malos.md y sigue su diagnóstico para
# corregirlo. Anota en un comentario aquí qué causó el error.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TAREA 3 (medio-difícil) — Refactorizar evaluate_model
#
# Pídele a la IA que separe el cálculo de la métrica de la parte de logging
# en evaluate_model, sin cambiar su firma de nodo (regressor, X_test, y_test).
# Usa el Caso 3: dile explícitamente qué NO debe cambiar.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TAREA 4 (difícil) — Manejo de errores en split_data
#
# Pídele a la IA que agregue una validación en split_data: si alguna columna
# de parameters["features"] no existe en el DataFrame, debe levantar un
# ValueError con el nombre de la columna faltante, en vez de que pandas
# falle más adelante con un KeyError genérico. Sigue el Caso 4. Después
# escribe un test (te apoyas en el Módulo 3) que confirme el nuevo error.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# PREGUNTAS DE REFLEXIÓN (respóndelas al terminar las cuatro tareas)
#
# 1. ¿En cuál tarea la IA propuso algo que rompía el contrato de inputs/
#    outputs de un nodo? ¿Cómo lo detectaste?
# 2. ¿Hubo alguna sugerencia que aceptaste sin entender del todo? ¿Qué
#    hiciste para entenderla antes de dejarla en tu proyecto?
# 3. ¿Qué tarea te habría tomado más tiempo sin IA, y por qué?
# ---------------------------------------------------------------------------
