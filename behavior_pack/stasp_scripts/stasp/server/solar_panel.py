# coding=utf-8
from ..common.constants import (
    ADVANCED_SOLAR_PANEL,
    HYBRID_SOLAR_PANEL,
    K_CHARGE_RF,
    K_CHARGE_RF_MAX,
    K_DISPLAY_NAME,
    K_LIGHT_LEVEL,
    K_MAX_OUTPUT,
    K_NIGHT_OUTPUT,
    K_OUTPUT_POWER,
    QUANTUM_SOLAR_PANEL,
    ULTIMATE_SOLAR_PANEL,
)
from ..common.modules import ImportModule

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


class AdvancedSolarPanelBase(BaseGenerator, ItemContainer, GUIControl):
    input_slots = (0,)
    output_slots = ()
    energy_io_mode = (1, 1, 1, 1, 1, 1)
    max_output = 0
    night_output = 0
    display_name = ""

    @SuperExecutorMeta.execute_super
    def __init__(self, dim, x, y, z, block_entity_data):
        self.t = 0
        self._light_level = 0
        self._power_output = 0
        self._charge_rf = 0
        self._charge_rf_max = 1
        self.bdata[K_MAX_OUTPUT] = self.max_output
        self.bdata[K_NIGHT_OUTPUT] = self.night_output
        self.bdata[K_DISPLAY_NAME] = self.display_name
        self.update_generation()
        self.update_charge_state()

    @SuperExecutorMeta.execute_super
    def OnTicking(self):
        self.t += 1
        if self.t % 5 == 0:
            self.charge_once()
        if self.t >= 20:
            self.t = 0
            self.update_generation()

    @SuperExecutorMeta.execute_super
    def OnSlotUpdate(self, slot_pos):
        if slot_pos == 0:
            self.update_charge_state()

    @SuperExecutorMeta.execute_super
    def OnUnload(self):
        pass

    def IsValidInput(self, slot, item):
        # type: (int, object) -> bool
        if slot != 0:
            return False
        return not (
            item.userData is None or GetIOPower(item.userData, -1, -1) == (-1, -1)
        )

    def update_generation(self):
        exposed = GetTopBlockHeight((self.x, self.z), self.dim) == self.y
        local_time = GetLocalTime(self.dim) % 24000
        light_level = (
            GetSkylightLevelRain(local_time)
            if IsRaining()
            else GetSkylightLevelClear(local_time)
        )
        self.light_level = max(0, light_level)
        if exposed:
            scaled = int(round(float(self.max_output) * self.light_level / 15.0))
            self.output_power = max(self.night_output, scaled)
        else:
            self.output_power = 0

    def update_charge_state(self):
        charge_item = self.GetSlotItem(0, get_user_data=True)
        if charge_item is None or charge_item.userData is None:
            self.charge_rf = 0
            self.charge_rf_max = 1
            return
        self.charge_rf, self.charge_rf_max = GetCharge(charge_item.userData)

    def charge_once(self):
        if (
            self.store_rf <= 0
            or self.charge_rf_max <= 1
            or self.charge_rf >= self.charge_rf_max
        ):
            return
        charged_item = self.GetSlotItem(0, get_user_data=True)
        if charged_item is None:
            return
        self.store_rf, _charged_in, self.charge_rf = ChargeItem(
            self.store_rf, charged_item, times=5
        )
        self.SetSlotItem(0, charged_item)

    @property
    def light_level(self):
        return self._light_level

    @light_level.setter
    def light_level(self, value):
        self.bdata[K_LIGHT_LEVEL] = self._light_level = value

    @property
    def output_power(self):
        return self._power_output

    @output_power.setter
    def output_power(self, value):
        self.bdata[K_OUTPUT_POWER] = self._power_output = value

    @property
    def charge_rf(self):
        return int(self._charge_rf) # NOTE: 可能需要 long

    @charge_rf.setter
    def charge_rf(self, value):
        self.bdata[K_CHARGE_RF] = self._charge_rf = float(value) # NOTE: 避免方块实体无法存 long 的 bug

    @property
    def charge_rf_max(self):
        return int(self._charge_rf_max) # NOTE: 可能需要 long

    @charge_rf_max.setter
    def charge_rf_max(self, value):
        self.bdata[K_CHARGE_RF_MAX] = self._charge_rf_max = float(value)


@RegisterMachine
class AdvancedSolarPanel(AdvancedSolarPanelBase):
    block_name = ADVANCED_SOLAR_PANEL
    display_name = "高级太阳能电池板"
    max_output, night_output, store_rf_max = 64, 8, 128000


@RegisterMachine
class HybridSolarPanel(AdvancedSolarPanelBase):
    block_name = HYBRID_SOLAR_PANEL
    display_name = "混合太阳能电池板"
    max_output, night_output, store_rf_max = 256, 32, 512000


@RegisterMachine
class UltimateSolarPanel(AdvancedSolarPanelBase):
    block_name = ULTIMATE_SOLAR_PANEL
    display_name = "终极太阳能电池板"
    max_output, night_output, store_rf_max = 1024, 128, 2048000


@RegisterMachine
class QuantumSolarPanel(AdvancedSolarPanelBase):
    block_name = QUANTUM_SOLAR_PANEL
    display_name = "量子太阳能电池板"
    max_output, night_output, store_rf_max = 4096, 512, 8192000
