# coding=utf-8
"""
按字符串路径导入前置模组 SkyblueTech 的模块。

附属包不能出现 `import skybluetech_scripts.xxx` 这类跨包 import 语句 —— 机审会把它
判为未知模块并告警。中转到 ModSDK 的 ImportModule 后, 语句里就不再出现跨包模块名。

ImportModule 在客户端与服务端分属两个 API 模块, 这里按当前所在侧选择, 因此本函数
只能在 tooldelta 初始化之后调用 (模组脚本加载时即已满足)。
"""
from stasp_scripts.tooldelta.internal import InServerEnv


def ImportModule(
    module_name,  # type: str
):
    if InServerEnv():
        import mod.server.extraServerApi as api
    else:
        import mod.client.extraClientApi as api

    return api.ImportModule(module_name)
