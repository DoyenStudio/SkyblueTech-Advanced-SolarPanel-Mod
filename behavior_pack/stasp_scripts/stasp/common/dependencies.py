# coding=utf-8
from stasp_scripts.tooldelta.events.basic import ClientEvent, ServerEvent


class SkyblueTechClientLoaded(ClientEvent):
    name = "SkyblueTechClientLoaded"
    def __init__(self): pass
    def marshal(self): pass
    @classmethod
    def unmarshal(cls, _): pass
    @classmethod
    def GetNamespace(cls): return "SkyblueTech"
    @classmethod
    def GetSystemName(cls): return "SkyblueTech.TDClient"


class SkyblueTechServerLoaded(ServerEvent):
    name = "SkyblueTechServerLoaded"
    def __init__(self): pass
    def marshal(self): pass
    @classmethod
    def unmarshal(cls, _): pass
    @classmethod
    def GetNamespace(cls): return "SkyblueTech"
    @classmethod
    def GetSystemName(cls): return "SkyblueTech.TDServer"
