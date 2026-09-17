# coding=utf-8
from stasp_scripts.tooldelta.mod_main import ToolDeltaMod, RegisterMod
from stasp_scripts import entry


@RegisterMod()
class SkyBlueTechAdvancedSolar(ToolDeltaMod):
    name = "SkyBlueTechAdvancedSolar"
    version = (1, 0, 0)

    def OnClientInited(self):
        entry.init_client()

    def OnServerInited(self):
        entry.init_server()
