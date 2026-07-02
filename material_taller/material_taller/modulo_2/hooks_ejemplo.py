"""Referencia — Hooks (sección 2.10).

Va en src/spaceflights/hooks.py dentro de tu proyecto. Se registra en
src/spaceflights/settings.py con:

    from spaceflights.hooks import RegistroDeNodos
    HOOKS = (RegistroDeNodos(),)
"""

import logging

from kedro.framework.hooks import hook_impl


class RegistroDeNodos:
    @hook_impl
    def before_node_run(self, node, catalog, inputs, is_async, run_id) -> None:
        logging.getLogger(__name__).info("Iniciando nodo: %s", node.name)

    @hook_impl
    def after_node_run(self, node, catalog, inputs, outputs, is_async, run_id) -> None:
        logging.getLogger(__name__).info("Nodo completado: %s", node.name)
