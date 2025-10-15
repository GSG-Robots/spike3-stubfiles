# type: ignore


def clear(port: int):
    """Schalte alle Pixel aus

    :param port: Port des Distance Sensors (:py:mod:`hub.port`)
    """


def set_pixel(port: int, x: int, y: int, pixel: int):
    """Setzt ein Pixel

    :param port: Port des Distance Sensors (:py:mod:`hub.port`)
    :param x: X-Koordinate des Pixels
    :param y: Y-Koordinate des Pixels
    :param pixel: Helligkeit in Prozent
    """


def get_pixel(port: int, x: int, y: int) -> int:
    """Liest ein Pixel aus

    :param port: Port des Distance Sensors (:py:mod:`hub.port`)
    :param x: X-Koordinate des Pixels
    :param y: Y-Koordinate des Pixels

    :returns: Helligkeit in Prozent
    """


def show(port: int, pixels: list[int]):
    """Zeigt ein Bild an

    :param port: Port des Distance Sensors (:py:mod:`hub.port`)
    :param pixels: Eine Liste von Pixeln, je bestehend aus der Helligkeit in Prozent
    """


def distance(port: int) -> int:
    """Liest die gemessene Entfernung aus

    :param port: Port des Distance Sensors (:py:mod:`hub.port`)
    :returns: Abstand in Millimetern, -1 für fehlgeschlagene Messung
    """
