# type: ignore

def clear(port: int):
    """Schalte alle Pixel aus

    :param port: Port der Color Matrix (:py:mod:`hub.port`)
    """


def set_pixel(port: int, x: int, y: int, pixel: tuple[int, int]):
    """Setzt ein Pixel

    :param port: Port der Color Matrix (:py:mod:`hub.port`)
    :param x: X-Koordinate des Pixels
    :param y: Y-Koordinate des Pixels
    :param pixel: Farbe aus :py:mod:`color` und Helligkeit in Prozent
    """


def get_pixel(port: int, x: int, y: int) -> tuple[int, int]:
    """Liest ein Pixel aus

    :param port: Port der Color Matrix (:py:mod:`hub.port`)
    :param x: X-Koordinate des Pixels
    :param y: Y-Koordinate des Pixels

    :returns pixel: Farbe aus :py:mod:`color` und Helligkeit in Prozent
    """


def show(port: int, pixels: list[tuple[int, int]]):
    """Zeigt ein Bild an

    :param port: Port der Color Matrix (:py:mod:`hub.port`)
    :param pixels: Eine Liste von Pixeln, je bestehend aus :py:mod:`color` und Helligkeit in Prozent
    """
