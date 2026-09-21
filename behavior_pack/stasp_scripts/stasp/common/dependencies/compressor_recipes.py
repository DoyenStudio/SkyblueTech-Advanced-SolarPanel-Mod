# coding=utf-8
from ..constants import IRRADIANT_URANIUM
from ..modules import ImportModule

_compressor_def = ImportModule(
    "skybluetech_scripts.skybluetech.common.machinery_def.compressor"
)
_compressor_jei = ImportModule(
    "skybluetech_scripts.skybluetech.common.mini_jei.machinery.compressor"
)

Input = _compressor_jei.Input
Output = _compressor_jei.Output

# 两端均导入, 将加工配方及 MiniJEI 索引一起注册到本体。
_compressor_def.recipes.add_recipe(
    _compressor_jei.CompressorRecipe(
        {
            0: Input("minecraft:glowstone_dust", 4),
            1: Input("skybluetech:uranium_dust", 1),
        },
        Output(IRRADIANT_URANIUM, 1),
        _compressor_def.DEFAULT_POWER,
        _compressor_def.DEFAULT_TICK_DURATION,
    )
)
