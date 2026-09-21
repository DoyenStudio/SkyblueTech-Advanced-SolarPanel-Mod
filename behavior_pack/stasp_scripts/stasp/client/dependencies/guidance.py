# coding=utf-8
from ...common.modules import ImportModule

# 前置模组的模块: 跨包 import 语句会被机审判为未知模块, 统一按字符串路径取。
_guidance = ImportModule(
    "skybluetech_scripts.skybluetech.client.export.guidance"
)

# 教程书入口: AddAddition(entry) 把 entry 挂到本体的 "附属模组" 目录下。
# entry 必须是 pages_define.MainTOCPageSection(图标物品, 图标数据值, 标题, 页面组),
# 不接受 TextPage 等页面对象; pages_define 另提供 PageGroup / MainTOCPage 等类型。
AddAddition = _guidance.AddAddition
pages_define = _guidance.pages_define
