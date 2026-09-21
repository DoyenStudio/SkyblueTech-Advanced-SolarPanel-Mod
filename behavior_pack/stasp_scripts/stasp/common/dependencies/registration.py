# coding=utf-8
from ..constants import DISPLAY_NAME, NAMESPACE
from ..modules import ImportModule

_REGISTRY_MODULE = "skybluetech_scripts.skybluetech.common.export.addon_registry"


def register_namespace():
    # type: () -> None
    registry = ImportModule(_REGISTRY_MODULE)
    if registry is None or not hasattr(registry, "RegisterAddonNamespace"):
        return
    registry.RegisterAddonNamespace(NAMESPACE, DISPLAY_NAME)
