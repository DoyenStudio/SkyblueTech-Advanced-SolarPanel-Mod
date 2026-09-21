# coding=utf-8
"""
本模组四块太阳能电池板的合成从工作台搬到前置模组的 机件加工台, 九宫格摆放与原配方一致。

本体机件加工台的配方表在运行时被逐个遍历, 这里直接往里追加, 免得本体反向依赖 stasp: 物品。
server/ 与 client/ 的 __init__ 都会导入本模块, 保证两端取到的都是填过配方的集合
(客户端 JEI 读的是同一份 recipes)。

电动版(自动化)在 import 时就快照了手动版的配方表, 所以要在它自己的集合上再追加一次,
否则电动加工台会漏掉这四条。两个集合装的是同一批配方对象, 本体的 RegisterRecipe 自带去重,
重复注册是安全的。
"""
from ..constants import (
    ADVANCED_SOLAR_PANEL,
    ENRICHED_SUNNARIUM,
    HYBRID_SOLAR_PANEL,
    IRRADIANT_GLASS_PANE,
    QUANTUM_CORE,
    QUANTUM_SOLAR_PANEL,
    ULTIMATE_SOLAR_PANEL,
)
from ..modules import ImportModule

# 前置模组的模块: 跨包 import 语句会被机审判为未知模块, 统一按字符串路径取。
_workstation_def = ImportModule(
    "skybluetech_scripts.skybluetech.common.machinery_def.machinery_workstation"
)
_electric_workstation_def = ImportModule(
    "skybluetech_scripts.skybluetech.common.machinery_def.electric_machinery_workstation"
)
_workstation_jei = ImportModule(
    "skybluetech_scripts.skybluetech.common.mini_jei.machinery.machinery_workstation"
)

Input = _workstation_jei.Input
MRecipe = _workstation_jei.MachineryWorkstationRecipe

# 槽位沿用本体加工台的 0-8 行优先排布, 与工作台九宫格一一对应。
# 第 3/4/5 个参数分别是所需扳手等级、钳等级(0=不需要, 1=铁及以上, 2=殷钢及以上)与加工次数。
_RECIPES = (
    # advanced solar panel  GGG / TST / CPC
    MRecipe(
        {
            0: Input(IRRADIANT_GLASS_PANE),
            1: Input(IRRADIANT_GLASS_PANE),
            2: Input(IRRADIANT_GLASS_PANE),
            3: Input("skybluetech:titanium_ingot"),
            4: Input("skybluetech:solar_panel"),
            5: Input("skybluetech:titanium_ingot"),
            6: Input("skybluetech:control_circuit_advanced"),
            7: Input("skybluetech:platinum_plate"),
            8: Input("skybluetech:control_circuit_advanced"),
        },
        ADVANCED_SOLAR_PANEL,
        MRecipe.LEVEL_IRON,
        MRecipe.LEVEL_IRON,
        8,
    ),
    # hybrid solar panel  PLP / TAT / CEC
    MRecipe(
        {
            0: Input("skybluetech:platinum_plate"),
            1: Input("minecraft:lapis_block"),
            2: Input("skybluetech:platinum_plate"),
            3: Input("skybluetech:titanium_ingot"),
            4: Input(ADVANCED_SOLAR_PANEL),
            5: Input("skybluetech:titanium_ingot"),
            6: Input("skybluetech:control_circuit_advanced"),
            7: Input(ENRICHED_SUNNARIUM),
            8: Input("skybluetech:control_circuit_advanced"),
        },
        HYBRID_SOLAR_PANEL,
        MRecipe.LEVEL_INVAR,
        MRecipe.LEVEL_INVAR,
        12,
    ),
    # ultimate solar panel  HHH / HPH / HHH
    MRecipe(
        {
            0: Input(HYBRID_SOLAR_PANEL),
            1: Input(HYBRID_SOLAR_PANEL),
            2: Input(HYBRID_SOLAR_PANEL),
            3: Input(HYBRID_SOLAR_PANEL),
            4: Input("skybluetech:control_circuit_professional"),
            5: Input(HYBRID_SOLAR_PANEL),
            6: Input(HYBRID_SOLAR_PANEL),
            7: Input(HYBRID_SOLAR_PANEL),
            8: Input(HYBRID_SOLAR_PANEL),
        },
        ULTIMATE_SOLAR_PANEL,
        MRecipe.LEVEL_INVAR,
        MRecipe.LEVEL_INVAR,
        16,
    ),
    # quantum solar panel  UUU / UQU / UUU
    MRecipe(
        {
            0: Input(ULTIMATE_SOLAR_PANEL),
            1: Input(ULTIMATE_SOLAR_PANEL),
            2: Input(ULTIMATE_SOLAR_PANEL),
            3: Input(ULTIMATE_SOLAR_PANEL),
            4: Input(QUANTUM_CORE),
            5: Input(ULTIMATE_SOLAR_PANEL),
            6: Input(ULTIMATE_SOLAR_PANEL),
            7: Input(ULTIMATE_SOLAR_PANEL),
            8: Input(ULTIMATE_SOLAR_PANEL),
        },
        QUANTUM_SOLAR_PANEL,
        MRecipe.LEVEL_INVAR,
        MRecipe.LEVEL_INVAR,
        24,
    ),
)

for _recipe in _RECIPES:
    _workstation_def.recipes.add_recipe(_recipe)
    _electric_workstation_def.recipes.add_recipe(_recipe)
