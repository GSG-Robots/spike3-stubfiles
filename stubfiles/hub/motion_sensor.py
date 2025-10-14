# type: ignore
"""
Konstanten für Gesten

* Angetippt (``hub.motion_sensor.TAPPED``)
* Doppelt angetippt (``hub.motion_sensor.DOUBLE_TAPPED``)
* Geschüttelt (``hub.motion_sensor.SHAKEN``)
* Fällt (``hub.motion_sensor.FALLING``)
* Unbekannt (``hub.motion_sensor.UNKNOWN``)

Konstanten für Seiten des Hubs

* Die Seite des SPIKE Prime Hubs mit der Lichtmatrix (``hub.motion_sensor.TOP``)
* Die Seite des SPIKE Prime Hubs, an der sich der Lautsprecher befindet (``hub.motion_sensor.FRONT``)
* Die rechte Seite des SPIKE Prime Hubs (von vorne betrachtet) (``hub.motion_sensor.RIGHT``)
* Die Seite des SPIKE Prime Hubs, wo sich der Akku befindet (``hub.motion_sensor.BOTTOM``)
* Die Seite des SPIKE Prime Hubs mit dem USB-Ladeanschluss (``hub.motion_sensor.BACK``)
* Die linke Seite des SPIKE Prime Hubs (von vorne betrachtet) (``hub.motion_sensor.LEFT``)
"""


TAPPED = 0
DOUBLE_TAPPED = 1
SHAKEN = 2
FALLING = 3
UNKNOWN = -1
TOP = 0
FRONT = 1
RIGHT = 2
BOTTOM = 3
BACK = 4
LEFT = 5

def acceleration(raw_unfiltered: bool) -> tuple[int, int, int]:
    """Lese die Beschleunigungswerte aus
    
    :param raw_unfiltered: Ob die Daten ungefiltert ausgegeben werden sollen
    
    :returns: Die x-, y- und z-Beschleunigungswerte in mG
    """

def angular_velocity(raw_unfiltered: bool) -> tuple[int, int, int]:
    """Lese die Winkelgeschwindigkeitswerte aus
    
    :param raw_unfiltered: Ob die Daten ungefiltert ausgegeben werden sollen
    
    :returns: Die x-, y- und z-Winkelgeschwindigkeitswerte in Dezigrad/s
    """

def gesture() -> int:
    """Liest die zuletzt erkannte Geste aus
    
    :returns: Eine Geste nach :py:mod:`hub.motion_sensor`
    """
    

