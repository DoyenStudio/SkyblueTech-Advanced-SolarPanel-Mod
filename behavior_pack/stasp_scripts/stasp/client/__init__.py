# coding=utf-8
from ..common.dependencies import charger_recipes  # noqa: F401 注册充能台配方
from ..common.dependencies import compressor_recipes  # noqa: F401 注册压缩机配方
from ..common.dependencies import workstation_recipes  # noqa: F401 注册机件加工台配方
from ..common.dependencies.registration import register_namespace
from . import solar_panel_ui

register_namespace()
