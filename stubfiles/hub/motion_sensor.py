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


def get_yaw_face() -> int:
    """Gibt an, orthogonal zu welcher Seite des Hubs die yaw-Achse befindlich ist.

    :returns: Eine Seite nach :py:mod:`hub.motion_sensor`
    """


def quaternion() -> tuple[float, float, float, float]:
    """Gibt die Quaternion der Hub-Ausrichtung an.

    :returns: Ein Tuple von w, x, y und z
    """


def up_face() -> int:
    """Gibt die Seite des Hubs zurück, die zurzeit nach oben zeigt.

    :returns: Eine Seite nach :py:mod:`hub.motion_sensor`
    """


def stable() -> bool:
    """Prüft, ob der Hub auf einer ebenen Fläche steht."""


def set_yaw_face(up: int) -> bool:
    """Ändere die Seite des Hubs, die als Gierebene benutzt wird. Wenn du den Hub so auf eine ebene Fläche stellst, dass diese Seite nach oben zeigt, wird nur der Gierwert aktualisiert, wenn du den Hub drehst.

    :param up: Die neue obere Seite
    """


def tap_count() -> int:
    """Gibt die Anzahl der Taps an, die seit dem Start des Programms oder dem letzten Aufruf von :py:meth:`~hub.motion_sensor.reset_tap_count` erkannt wurden."""


def reset_tap_count():
    """Setz die Tap-Anzahl zurück, die von der Funktion :py:meth:`~hub.motion_sensor.tap_count` (Tap-Anzahl) zurückgegeben wird."""


def tilt_angles() -> tuple[int, int, int]:
    """Gibt ein Tupel zurück, das Gier-, Neigungs- und Rollwerte als ganze Zahlen enthält.

    :returns: Gier-, Neigungs- und Rollwinkel in Dezigrad
    """


def reset_yaw(angle: int):
    """Ändere den Versatz des Gierwinkels. Der eingestellte Winkel ist der neue Gierwert."""
