# type: ignore

from . import button
from . import light_matrix
from . import light
from . import motion_sensor
from . import port
from . import sound


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


__all__ = [
    "button",
    "light_matrix",
    "light",
    "motion_sensor",
    "port",
    "sound",
    "device_uuid",
    "hardware_id",
    "power_off",
    "temperature",
]
