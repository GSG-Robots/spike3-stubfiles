# type: ignore

def color(port: int) -> int:
    """Gibt die erkannte Farbe an

    :param port: Port des Color Sensors (:py:mod:`hub.port`)

    :returns: Ein Element aus :py:mod:`color`
    """


def reflection(port: int) -> int:
    """Gibt die Intensität des reflektierten Lichts an.

    :param port: Port des Color Sensors (:py:mod:`hub.port`)

    :returns: Eine Prozentzahl
    """


def rgbi(port: int) -> tuple[int, int, int, int]:
    """Gibt die gemessenen RGB-Werte und Intensität des reflektierten Lichts an.

    :param port: Port des Color Sensors (:py:mod:`hub.port`)

    :returns: Ein Tupel des Rot-, Grün-, und Blauwerts der Farbe und der Intensität
    """
