# type: ignore

"""
Konstanten für LEDs

* POWER (``hub.light.POWER``)
* CONNECT (``hub.light.CONNECT``)
"""

POWER = 0
CONNECT = 1


def color(light: int, color: int):
    """Stelle die Farbe der LED ein. :py:const:`color.BLACK` für aus.

    :param light: Die betroffene LED (:py:mod:`hub.light`)
    :param color: Die Farbe (:py:mod:`color`)
    """
