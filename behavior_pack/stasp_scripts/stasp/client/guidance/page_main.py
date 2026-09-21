# coding=utf-8
from stasp_scripts.stasp.common import constants

from ..dependencies.guidance import AddAddition, pages_define


# 目录项要回指 asp_machinery 分组本身, 而分组对象要等 PageGroup 构造完才存在。
# 这里不能像点击回调那样用 lambda 延迟求值: PageGroup 构造时就会遍历页面调用
# TOCPage.SetGroup, 其中的 s.link_to.GetParent() 只认 PageGroup, 收到函数会抛
# AttributeError。所以先建组, 再用 AddSection 补目录项。
asp_machinery_toc = pages_define.TOCPage([], "asp_machinery_toc")
asp_machinery = pages_define.PageGroup(
    "asp_machinery",
    [
        asp_machinery_toc,
        pages_define.MachineryWorkstationRecipePage(constants.ADVANCED_SOLAR_PANEL),
        pages_define.MachineryWorkstationRecipePage(constants.HYBRID_SOLAR_PANEL),
        pages_define.MachineryWorkstationRecipePage(constants.ULTIMATE_SOLAR_PANEL),
        pages_define.MachineryWorkstationRecipePage(constants.QUANTUM_SOLAR_PANEL),
    ],
)
# link_page_index 是分组内的页面下标; 书本每屏渲染两页, FastJump 会向下取偶数页
for _panel_item_id, _page_index in (
    (constants.ADVANCED_SOLAR_PANEL, 1),
    (constants.HYBRID_SOLAR_PANEL, 2),
    (constants.ULTIMATE_SOLAR_PANEL, 3),
    (constants.QUANTUM_SOLAR_PANEL, 4),
):
    asp_machinery_toc.AddSection(
        pages_define.TOCPageSection(
            _panel_item_id, 0, None, asp_machinery, _page_index
        )
    )
asp_credits = pages_define.PageGroup(
    "asp_credits",
    [
        pages_define.TextPage(
            "第三方说明",
            "本模组移植自 Java 版模组《高级太阳能》（ReAdvSolarPanels） ， 依赖《蔚蓝科技》作为前置模组， 其使用 MIT 开源协议。",
        )
    ],
)
asp_main = pages_define.PageGroup(
    "asp_main",
    [
        pages_define.TextPage(
            "高级太阳能",
            '《高级太阳能》为《蔚蓝科技》扩展了<text color="§9" t="能量利用效率更高、 输出功率更大">的太阳能， 它们甚至能在<text color="§1" t="晚上">利用月光等微光进行发电！\n\n在 Mini-JEI 中选择<text color="§2" t="高级太阳能">分组即可查看本模组所有物品的配方。',
        ),
        pages_define.MainTOCPage(
            [
                pages_define.MainTOCPageSection(
                    constants.ADVANCED_SOLAR_PANEL,
                    0,
                    "太阳能列表",
                    asp_machinery,
                ),
                pages_define.MainTOCPageSection(
                    "minecraft:music_disc_cat", 0, "第三方说明", asp_credits
                ),
            ]
        ),
    ],
)

AddAddition(
    pages_define.MainTOCPageSection(
        constants.ADVANCED_SOLAR_PANEL,
        0,
        "高级太阳能",
        asp_main,
    )
)
