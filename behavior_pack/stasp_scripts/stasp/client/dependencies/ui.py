# coding=utf-8
from ...common.modules import ImportModule

# 前置模组的模块: 跨包 import 语句会被机审判为未知模块, 统一按字符串路径取。
_client_api = ImportModule("skybluetech_scripts.tooldelta.api.client")
_machinery_def = ImportModule(
    "skybluetech_scripts.skybluetech.common.machinery_def.basic"
)
_td_nbt = ImportModule("skybluetech_scripts.tooldelta.utils.nbt")
_td_ui = ImportModule("skybluetech_scripts.tooldelta.ui")
_ui_define = ImportModule(
    "skybluetech_scripts.skybluetech.client.ui.machinery.define"
)
_ui_utils = ImportModule(
    "skybluetech_scripts.skybluetech.client.ui.machinery.utils"
)
_utils_py_comp = ImportModule("skybluetech_scripts.tooldelta.utils.py_comp")

GetBlockEntityData = _client_api.GetBlockEntityData
K_STORE_RF = _machinery_def.K_STORE_RF
GetValue = _td_nbt.GetValueWithDefault
RegistToolDeltaScreen = _td_ui.RegistToolDeltaScreen
MAIN_PATH = _ui_define.MAIN_PATH
MachinePanelUIProxy = _ui_define.MachinePanelUIProxy
UpdateGenericProgressT2B = _ui_utils.UpdateGenericProgressT2B
UpdatePowerBar = _ui_utils.UpdatePowerBar
py2_long = _utils_py_comp.py2_long
