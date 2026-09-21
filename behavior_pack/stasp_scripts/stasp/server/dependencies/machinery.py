# coding=utf-8
from ...common.modules import ImportModule

# 前置模组的模块: 跨包 import 语句会被机审判为未知模块, 统一按字符串路径取。
_charge_util = ImportModule(
    "skybluetech_scripts.skybluetech.server.machinery.utils.charge"
)
_machinery_basic = ImportModule(
    "skybluetech_scripts.skybluetech.server.machinery.basic"
)
_server_api = ImportModule("skybluetech_scripts.tooldelta.api.server")
_solar_panel_util = ImportModule(
    "skybluetech_scripts.skybluetech.server.machinery.solar_panel"
)
_super_executor = ImportModule(
    "skybluetech_scripts.tooldelta.extensions.super_executor"
)

ChargeItem = _charge_util.ChargeItem
GetCharge = _charge_util.GetCharge
GetIOPower = _charge_util.GetIOPower

BaseGenerator = _machinery_basic.BaseGenerator
GUIControl = _machinery_basic.GUIControl
ItemContainer = _machinery_basic.ItemContainer
RegisterMachine = _machinery_basic.RegisterMachine

GetLocalTime = _server_api.GetLocalTime
GetTopBlockHeight = _server_api.GetTopBlockHeight
IsRaining = _server_api.IsRaining

GetSkylightLevelClear = _solar_panel_util.GetSkylightLevelClear
GetSkylightLevelRain = _solar_panel_util.GetSkylightLevelRain

SuperExecutorMeta = _super_executor.SuperExecutorMeta
