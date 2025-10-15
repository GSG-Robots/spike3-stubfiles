# type: ignore

from typing import Awaitable, Callable


def run(*functions: Awaitable) -> None:
    """Starte beliebig viele parallele asynchrone Funktionen vom Typ async. Diese Funktion solltest du zur Erstellung von Programmen verwenden, die ähnlich wie Textblöcke strukturiert sind.

    :param *functions: Die auszuführenden Funktionen
    """


async def sleep_ms(duration: int):
    """Unterbreche die Ausführung der Anwendung

    :param duration: Die Dauer in Millisekunden
    """


async def until(function: Callable[[], bool], timeout: int = 0):
    """Warte bis der Wert der angegebenen Funktion :py:const:``True`` oder die Zeit abgelaufen ist.

    :param function: Die Bedingung als Funktion
    :param timeout: Die maximale Zeit, die gewartet wird
    """
