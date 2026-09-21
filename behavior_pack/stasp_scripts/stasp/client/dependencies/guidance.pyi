# coding=utf-8
# 类型桩, 仅供 Pylance / Pyright 读取; 运行时实现是同目录的 guidance.py。
#
# 运行时代码不能写跨包 import (机审会告警), 只能用 ImportModule 按字符串路径取模块,
# 拿到的对象因此没有类型。这里把真正的类型补回来, 让调用处能补全和跳转。
# 本文件不会被游戏加载执行, 也不会进入任何运行期代码路径。
#
# 依赖工作区设置 python.analysis.extraPaths 里的
# d:/addon/skybluetech/behavior_pack, 否则 skybluetech_scripts 解析不出来。
from skybluetech_scripts.skybluetech.client.export.guidance import (
    AddAddition as AddAddition,
    pages_define as pages_define,
)
