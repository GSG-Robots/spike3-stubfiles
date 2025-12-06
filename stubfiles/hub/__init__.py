# type: ignore

from . import button, light, light_matrix, motion_sensor, port, sound


def device_uuid() -> str:
    """Ruft die Gerätekennung ab."""


def hardware_id() -> str:
    """Ruft die Hardware-Kennung ab"""


def power_off() -> int:
    """Schalte den Hub aus

    :returns: Unbekannt
    """


def temperature() -> int:
    """Ruft die Hub-Temperatur ab.

    :returns: Temperatur in 1/10 Grad Celsius (°C)
    """


def battery_voltage() -> int:
    """Ruft die Batteriespannung ab.

    :returns: Batteriespannung in mV
    """


__all__ = [
    "button",
    "device_uuid",
    "hardware_id",
    "light",
    "light_matrix",
    "motion_sensor",
    "port",
    "power_off",
    "sound",
    "temperature",
]
