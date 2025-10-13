"""Konstanten für Motor-Zustände

* READY
* RUNNING
* STALLED
* CANCELED
* ERROR
* DISCONNECTED

Konstanten für Motor-Bremsverhalten

* CONTINUE
* COAST
* BRAKE
* HOLD
* SMART_COAST
* SMART_BRAKE

Konstanten für Motor-Drehrichtungen

* CLOCKWISE
* COUNTERCLOCKWISE
* SHORTEST_PATH
* LONGEST_PATH
"""

# state-Konstanten
READY = 1
RUNNING = 2
STALLED = -1
CANCELED = -2
ERROR = -3
DISCONNECTED = 0

# stop-Konstanten
CONTINUE = 0
COAST = 1
BRAKE = 2
HOLD = 3
SMART_COAST = 4
SMART_BRAKE = 5

# Richtungs-Konstanten
CLOCKWISE = 0
COUNTERCLOCKWISE = 1
SHORTEST_PATH = 2
LONGEST_PATH = 3


def absolute_position(port: int) -> int:
    """Ruft die absolute Position eines Motors ab

    :param port: Port des Motors (:py:mod:`hub.port`)
    """


def relative_position(port: int) -> int:
    """Ruft die relative Position eines Motors ab

    :param port: Port des Motors (:py:mod:`hub.port`)
    """


def reset_relative_position(port: int, position: int):
    """Ändere die Position, die als Offset dient, wenn die Funktion :py:func:`~motor.run_to_relative_position` verwendet wird.

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param position: Die Position, die gesetzt werden soll
    """


def get_duty_cycle(port: int) -> int:
    """Ruft die PWM eines Motors ab

    :param port: Port des Motors (:py:mod:`hub.port`)
    """


def set_duty_cycle(port: int, duty_cycle: int):
    """Setze die PWM eines Motors

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param duty_cycle: PWM, -10000 bis 10000
    """


def run(port: int, velocity: int, *, acceleration: int = 1000):
    """Starte den Motor

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    """


def run_for_degrees(
    port: int,
    degrees: int,
    velocity: int,
    *,
    stop: int = BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000,
):
    """Drehe den Motor für eine gewisse Gradzahl

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param degrees: Die Anzahl an Grad
    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def run_for_time(
    port: int,
    duration: int,
    velocity: int,
    *,
    stop: int = BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000,
):
    """Drehe den Motor für eine gewisse Gradzahl

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param duration: Die Dauer in Millisekunden
    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def run_to_relative_position(
    port: int,
    position: int,
    velocity: int,
    *,
    stop: int = BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000,
):
    """Drehe den Motor auf eine relative Position

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param position: Die Gradzahl
    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def run_to_absolute_position(
    port: int,
    position: int,
    velocity: int,
    *,
    stop: int = BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000,
):
    """Drehe den Motor auf eine absolute Position

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param position: Die Gradzahl
    :param velocity: Die Geschwindigkeit in Grad/s. Wertebereiche siehe :doc:`/motors`
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    :param acceleration: Die Beschleunigung in Grad/s². 1 - 10000
    :param deceleration: Die Entschleunigung in Grad/s². 1 - 10000
    """


def stop(port: int, *, stop: int = BRAKE):
    """Motor stoppen

    :param port: Port des Motors (:py:mod:`hub.port`)
    :param stop: Die Brems-Methode. Siehe :doc:`/api/motor`
    """


def velocity(port: int) -> int:
    """Ruf die Geschwindigkeit (Grad/s) eines Motors ab

    :param port: Port des Motors (:py:mod:`hub.port`)
    """
