import motor

"""
Konstanten für Motor-Paare

* PAIR_1
* PAIR_2
* PAIR_3
"""

PAIR_1: int = 0
PAIR_2: int = 1
PAIR_3: int = 2


def move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000):
    """Fahre mit dem Motor-Paar

    :param pair: Das betroffene Motor-Paar
    :param steering: Die Lenkrichtung in Prozent, -100 bis 100

    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    """


def move_for_degrees(
    pair: int,
    degrees: int,
    steering: int,
    *,
    velocity: int = 360,
    acceleration: int = 1000,
):
    """Fahre mit dem Motor-Paar

    :param pair: Das betroffene Motor-Paar
    :param degrees: Die Anzahl an Grad
    :param steering: Die Lenkrichtung in Prozent, -100 bis 100

    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def move_for_time(
    pair: int,
    duration: int,
    steering: int,
    *,
    velocity: int = 360,
    acceleration: int = 1000,
):
    """Fahre mit dem Motor-Paar

    :param pair: Das betroffene Motor-Paar
    :param duration: Die Dauer in Millisekunden
    :param steering: Die Lenkrichtung in Prozent, -100 bis 100

    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def move_tank(
    pair: int,
    left_velocity: int,
    right_velocity: int,
    *,
    velocity: int = 360,
    acceleration: int = 1000,
):
    """Fahre mit dem Motor-Paar, gedacht für Drehungen auf der Stelle

    :param pair: Das betroffene Motor-Paar
    :param left_velocity: Die Geschwindigkeit des linken Motors in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param right_velocity: Die Geschwindigkeit des rechten Motors in Grad/s. Wertebereiche siehe :doc:`/motors`

    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    """


def move_tank_for_degrees(
    pair: int,
    degrees: int,
    left_velocity: int,
    right_velocity: int,
    *,
    velocity: int = 360,
    acceleration: int = 1000,
):
    """Fahre mit dem Motor-Paar, gedacht für Drehungen auf der Stelle

    :param pair: Das betroffene Motor-Paar
    :param degrees: Die Anzahl an Grad
    :param left_velocity: Die Geschwindigkeit des linken Motors in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param right_velocity: Die Geschwindigkeit des rechten Motors in Grad/s. Wertebereiche siehe :doc:`/motors`

    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def move_tank_for_time(
    pair: int,
    duration: int,
    left_velocity: int,
    right_velocity: int,
    *,
    velocity: int = 360,
    acceleration: int = 1000,
):
    """Fahre mit dem Motor-Paar, gedacht für Drehungen auf der Stelle

    :param pair: Das betroffene Motor-Paar
    :param duration: Die Dauer in Millisekunden
    :param left_velocity: Die Geschwindigkeit des linken Motors in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param right_velocity: Die Geschwindigkeit des rechten Motors in Grad/s. Wertebereiche siehe :doc:`/motors`

    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def pair(pair: int, left_motor: int, right_motor: int):
    """Kopple zwei Motoren zu einem Motor-Paar.

    :param pair: Das betroffene Motor-Paar
    :param left_motor: Der Port am linken Motor (:py:mod:`hub.port`)
    :param right_motor: Der Port am rechten Motor (:py:mod:`hub.port`)
    """


def stop(pair: int, *, stop=motor.BRAKE):
    """Stoppe ein Motor-Paar.

    :param pair: Das betroffene Motor-Paar
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    """


def unpair(pair: int):
    """Entkopple ein Motor-Paar.

    :param pair: Das betroffene Motor-Paar
    """
