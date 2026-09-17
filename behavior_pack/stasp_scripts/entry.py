# coding=utf-8


def init_server():
    from mod.server.extraServerApi import ImportModule
    from stasp_scripts.stasp.common.dependencies import SkyblueTechServerLoaded

    @SkyblueTechServerLoaded.Listen()
    def on_skybluetech_server_loaded(_):
        from stasp_scripts.stasp import server

    if ImportModule("skybluetech_scripts") is not None:
        on_skybluetech_server_loaded(SkyblueTechServerLoaded())


def init_client():
    from mod.client.extraClientApi import ImportModule
    from stasp_scripts.stasp.common.dependencies import SkyblueTechClientLoaded

    @SkyblueTechClientLoaded.Listen()
    def on_skybluetech_client_loaded(_):
        from stasp_scripts.stasp import client

    if ImportModule("skybluetech_scripts") is not None:
        on_skybluetech_client_loaded(SkyblueTechClientLoaded())
