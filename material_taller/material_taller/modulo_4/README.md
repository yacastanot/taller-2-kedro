# Material complementario — Módulo 4

Material para el Módulo 4: IA en el IDE aplicada a un proyecto Kedro.

## Qué hay adentro

`prompts_buenos_vs_malos.md` tiene los cuatro casos típicos (agregar un nodo,
debuggear un error de pipeline, refactorizar un nodo, agregar manejo de
errores) pero llevados al vocabulario de Kedro: nodos, contratos de
inputs/outputs, `catalog.yml`, tracebacks de `DatasetError`.

`ejercicio_ia.py` es el enunciado de las cuatro tareas del ejercicio práctico
de la sección 4.4, para resolver sobre tu propio proyecto `spaceflights` de
los Módulos 1-3.

`issue_entrega_template.txt` es el texto del Issue de entrega (sección 4.6).
Lo usas solo cuando estés listo para entregar el taller completo — el archivo
te indica dónde crear el Issue en tu repo y qué pegar como contenido.

## Cómo trabajar el módulo

Si ya usaste un asistente de IA en el Módulo 4 del Taller 1, la mecánica es la
misma — la diferencia es que ahora tu código vive dentro de un framework con
reglas propias (nodos, catálogo, pipelines), así que la IA necesita más
contexto explícito para no romper esas reglas. Lee primero
`prompts_buenos_vs_malos.md`, después trabaja `ejercicio_ia.py` tarea por
tarea sobre tu proyecto real.

## La regla que vale repetir

La IA propone, tú decides — y en Kedro eso importa más que en un script
suelto, porque un nodo mal formado no falla ahí mismo: falla cuando Kedro
intenta conectar sus inputs/outputs con el resto del pipeline, a veces varios
nodos más adelante. Si una sugerencia cambia la firma de un nodo o el nombre
de un dataset, verifica siempre contra tu `catalog.yml` antes de aceptarla.
