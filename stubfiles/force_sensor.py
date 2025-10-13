def force(port: int) -> int:
    """Liest die gemessene Druckkraft auf den Force Sensor aus

    :param port: Port des Force Sensors (:py:mod:`hub.port`)
    :returns: Kraft in Prozent
    """


def raw(port: int) -> int:
    """Liest die ungefilterte und nicht kalibrierte Druckkraft vom Force Sensor aus

    :param port: Port des Force Sensors (:py:mod:`hub.port`)
    :returns: Kraft in Prozent
    """


def pressed(port: int) -> bool:
    """Liest aus, ob der Sensor gedrückt wird

    :param port: Port des Force Sensors (:py:mod:`hub.port`)
    """
