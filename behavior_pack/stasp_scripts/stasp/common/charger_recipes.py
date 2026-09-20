# coding=utf-8
from .modules import ImportModule

# 前置模组的模块: 跨包 import 语句会被机审判为未知模块, 统一按字符串路径取。
_charger_def = ImportModule(
    "skybluetech_scripts.skybluetech.common.machinery_def.charger"
)
_charger_jei = ImportModule(
    "skybluetech_scripts.skybluetech.common.mini_jei.machinery.charger"
)

# 本体充能台的配方表在运行时被 Processor 逐个遍历, 这里直接往里追加,
# 免得本体反向依赖 stasp: 物品。server/ 与 client/ 的 __init__ 都会导入本模块,
# 保证两端取到的都是填过这条配方的集合 (客户端 JEI 读的是同一份 recipes)。
_charger_def.recipes.add_recipe(
    _charger_jei.gen_preset_recipe(2000, 2560)(
        "minecraft:glowstone", 1, "stasp:sunnarium_part", 1
    )
)
