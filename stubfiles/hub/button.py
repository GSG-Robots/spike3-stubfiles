# type: ignore

"""
Konstanten für Knöpfe

* LEFT (``hub.button.LEFT``)
* RIGHT (``hub.button.RIGHT``)
* POWER (``hub.button.POWER``)
* CONNECT (``hub.button.CONNECT``)
"""

POWER = 0
LEFT = 1
RIGHT = 2
CONNECT = 3


def pressed(button: int) -> int:
    """Gibt an, ob der gefragte Knopf gedrückt ist.
    
    :param button: Der gefragte Button (:py:mod:`hub.button`)
    :returns: Für wie viele Millisekunden der Knopf bisher gedrückt gehalten wurde, oder :py:const:`0` falls nicht
    """
