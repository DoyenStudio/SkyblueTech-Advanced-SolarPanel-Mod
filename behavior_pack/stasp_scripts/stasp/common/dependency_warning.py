# coding=utf-8
# 前置模组 SkyblueTech (蔚蓝科技) 未加载时, 周期性在聊天栏提示玩家。
#
# 本模块由 entry.init_server() 导入, 存在的意义就是跑在"前置未加载"这条退化路径上,
# 因此只允许依赖本附属包自己的 tooldelta —— 不得导入 stasp.server, 也不得触碰前置模组。
#
# 只在服务端导入: 下面的 .Listen() 挂在服务端事件上, 客户端不得引用本模块。

from stasp_scripts.tooldelta.api.common.timer import Repeat
from stasp_scripts.tooldelta.events.server import (
    ClientLoadAddonsFinishServerEvent,
    LoadServerAddonScriptsAfter,
)

from .constants import DISPLAY_NAME
from .modules import ImportModule

_PREREQUISITE = "skybluetech_scripts"

# NOTE: AddRepeatedTimer 的 delay 单位是秒而非 tick。按 tick 口径填写会让 30 秒变成 10 分钟。
_INTERVAL_SECONDS = 30.0

_WARNING = (
    "§7[§6!§7] §c《§6"
    + DISPLAY_NAME
    + "§c》缺少前置模组《§6蔚蓝科技§c》, 已停止工作。"
    + "\n§7[§6!§7] 请启用前置模组后重新进入世界。"
)

_armed = False  # 循环定时器已挂上
_resolved = False  # 已确认前置模组在场
_loaded = False  # 前置模组握手已完成


def mark_loaded():
    # type: () -> None
    """前置模组已就位, 停止告警。由 entry 的握手回调调用。"""
    global _loaded
    _loaded = True


def _notify(player_id):
    # type: (str) -> None
    # 延迟导入: 本模块由 init_server() 导入, 引擎组件导入失败不能连累健康环境的启动。
    from stasp_scripts.tooldelta.api.server import NotifyOneMessage

    NotifyOneMessage(player_id, _WARNING) 


@Repeat(_INTERVAL_SECONDS)
def _warn_all():
    # type: () -> None
    if _loaded:
        return
    from stasp_scripts.tooldelta.api.server import GetAllPlayers

    for player_id in GetAllPlayers():
        _notify(player_id)


# # NOTE: Repeat 只返回包装函数, 不会挂表 —— 必须显式调用 _arm_warning() 才真正注册定时器。
# _arm_warning = Repeat(_INTERVAL_SECONDS)(_warn_all)


def start():
    # type: () -> None
    """确认前置模组仍然未加载后, 挂上聊天栏循环告警。"""
    global _armed, _resolved
    if _armed or _loaded or _resolved:
        return
    if ImportModule(_PREREQUISITE) is not None:
        _resolved = True
        return
    _armed = True
    _warn_all()


@LoadServerAddonScriptsAfter.Listen()
def _on_server_addon_scripts_loaded(_):
    # type: (LoadServerAddonScriptsAfter) -> None
    # 此刻世界必然已起, CreateGame(GetLevelId()) 才可用。
    start()


@ClientLoadAddonsFinishServerEvent.Listen()
def _on_client_load_addons_finish(event):
    # type: (ClientLoadAddonsFinishServerEvent) -> None
    # 此刻客户端 UI 已就绪, 聊天栏才开始显示消息 —— 进服第一刻就提示。
    # 顺带兜底: 若上面那个监听注册得比 LoadServerAddonScriptsAfter 还晚, 在这里补挂。
    if _loaded:
        return
    if not _armed:
        start()
    if _armed:
        _notify(event.playerId)
