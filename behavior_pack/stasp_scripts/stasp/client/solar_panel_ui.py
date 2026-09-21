# coding=utf-8
from ..common.constants import (
    K_CHARGE_RF,
    K_CHARGE_RF_MAX,
    K_DISPLAY_NAME,
    K_LIGHT_LEVEL,
    K_MAX_OUTPUT,
    K_NIGHT_OUTPUT,
    K_OUTPUT_POWER,
)
from .dependencies.ui import (
    GetBlockEntityData,
    GetValue,
    K_STORE_RF,
    MAIN_PATH,
    MachinePanelUIProxy,
    py2_long,
    RegistToolDeltaScreen,
    UpdateGenericProgressT2B,
    UpdatePowerBar,
)

LABEL_PATH = MAIN_PATH / "machine_label"
POWER_PATH = MAIN_PATH / "power_bar"
SUN_PATH = MAIN_PATH / "sun_progress"
TEXT_PATH = MAIN_PATH / "status_text"
CHARGE_PATH = MAIN_PATH / "charge_text"


@RegistToolDeltaScreen("STASPSolarPanelUI.main", is_proxy=True)
class AdvancedSolarPanelUI(MachinePanelUIProxy):
    def OnCreate(self):
        self.machine_label = self.GetElement(LABEL_PATH).asLabel()
        self.power_bar = self.GetElement(POWER_PATH)
        self.sun = self.GetElement(SUN_PATH)
        self.status_text = self.GetElement(TEXT_PATH).asLabel()
        self.charge_text = self.GetElement(CHARGE_PATH).asLabel()

    def OnTicking(self):
        data = GetBlockEntityData(*self.pos[1:])
        if data is None:
            return
        data = data["exData"]
        store_rf = GetValue(data, K_STORE_RF, 0)
        max_output = GetValue(data, K_MAX_OUTPUT, 1)
        night_output = GetValue(data, K_NIGHT_OUTPUT, 0)
        light_level = GetValue(data, K_LIGHT_LEVEL, 0)
        output_power = GetValue(data, K_OUTPUT_POWER, 0)
        charge_rf = GetValue(data, K_CHARGE_RF, 0)
        charge_rf_max = GetValue(data, K_CHARGE_RF_MAX, -1)
        display_name = GetValue(data, K_DISPLAY_NAME, "高级太阳能电池板")
        self.machine_label.SetText(display_name)
        UpdatePowerBar(self.power_bar, store_rf, max_output * 2000)
        UpdateGenericProgressT2B(self.sun, float(light_level) / 15)
        self.status_text.SetText(
            "太阳光强度: %d MCLux\n当前输出: %d RF/t"
            % (light_level, output_power)
        )
        if charge_rf_max <= 1:
            self.charge_text.SetText("未放入可充能装备或电池")
        else:
            self.charge_text.SetText("%d / %d RF" % (py2_long(charge_rf), py2_long(charge_rf_max)))
