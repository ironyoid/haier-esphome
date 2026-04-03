import esphome.codegen as cg
from esphome.components import select, sensor
import esphome.config_validation as cv
from esphome.const import (
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    UNIT_MINUTE,
)

from ..climate import (
    CONF_HAIER_ID,
    HaierClimateBase,
    haier_ns,
)

CODEOWNERS = ["@paveldn"]
SleepTimerSelect = haier_ns.class_("SleepTimerSelect", select.Select)

CONF_SLEEP_TIMER = "sleep_timer"
CONF_SLEEP_TIMER_COUNTDOWN = "sleep_timer_countdown"

ICON_TIMER = "mdi:timer-outline"
ICON_TIMER_SAND = "mdi:timer-sand"

SLEEP_TIMER_OPTIONS = [
    "Off",
    "0.5h",
    "1h",
    "2h",
    "3h",
    "4h",
    "5h",
    "6h",
    "8h",
    "10h",
    "12h",
    "24h",
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_HAIER_ID): cv.use_id(HaierClimateBase),
        cv.Optional(CONF_SLEEP_TIMER): select.select_schema(
            SleepTimerSelect,
            icon=ICON_TIMER,
            entity_category=ENTITY_CATEGORY_CONFIG,
        ),
        cv.Optional(CONF_SLEEP_TIMER_COUNTDOWN): sensor.sensor_schema(
            unit_of_measurement=UNIT_MINUTE,
            icon=ICON_TIMER_SAND,
            accuracy_decimals=0,
            entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        ),
    }
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_HAIER_ID])
    if conf := config.get(CONF_SLEEP_TIMER):
        sel = await select.new_select(conf, options=SLEEP_TIMER_OPTIONS)
        await cg.register_parented(sel, parent)
        cg.add(parent.set_sleep_timer_select(sel))
    if conf := config.get(CONF_SLEEP_TIMER_COUNTDOWN):
        sens = await sensor.new_sensor(conf)
        cg.add(parent.set_sleep_timer_countdown_sensor(sens))
