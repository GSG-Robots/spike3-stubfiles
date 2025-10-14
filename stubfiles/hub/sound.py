# type: ignore

"""
Konstanten für Kanäle

* Irgendeine (wozu?) (``hub.sound.ANY``)
* Standard (``hub.sound.DEFAULT``)

Konstanten für Wellenformen

* :wikipedia:`Sine wave` (``hub.sound.WAVEFORM_SINE``)
* :wikipedia:`Sawtooth wave` (``hub.sound.WAVEFORM_SAWTOOTH``)
* :wikipedia:`Square wave (waveform)` (``hub.sound.WAVEFORM_SQUARE``)
* :wikipedia:`Triangle wave` (``hub.sound.WAVEFORM_TRIANGLE``)
"""

ANY = -2
DEFAULT = -1
WAVEFORM_SINE = 1
WAVEFORM_SAWTOOTH = 3
WAVEFORM_SQUARE = 2
WAVEFORM_TRIANGLE = 1


def beep(
    frequency: int = 440,
    duration: int = 500,
    volume: int = 100,
    *,
    attack: int = 0,
    decay: int = 0,
    sustain: int = 100,
    release: int = 0,
    transition: int = 10,
    waveform: int = WAVEFORM_SINE,
    channel: int = DEFAULT,
):
    """Starte einen Piepton am Hub
    
    :param frequency: Frequenz in Hz
    :param duration: Dauer
    :param volume: Lautstärke in Prozent
    
    :param attack: Die Dauer des Hochfahrens von Null bis zum Spitzenwert ab dem Zeitpunkt, wenn die Taste gedrückt wird.
    :param decay: Die Dauer des anschließenden Rundowns vom Attack-Pegel auf den vorgesehenen Sustain-Pegel.
    :param sustain: Der Pegel während der Hauptsequenz der Tondauer, bis die Taste losgelassen wird.
    :param release: Die Dauer, bis der Pegel nach dem Loslassen der Taste vom Sustain-Pegel auf Null abfällt.
    :param transition: Zeit in Millisekunden bis zum Übergang in den Ton, wenn bereits etwas im Kanal abgespielt wird.
    :param waveform: Die synthetisierte Wellenform. Verwende eine der Konstanten im Modul :py:mod:`hub.sound`.
    :param channel: Der fürs Abspielen gewünschte Kanal. Die Optionen sind :py:const:`hub.sound.DEFAULT` und :py:const:`hub.sound.ANY`
    """

def stop():
    """Stoppe alle Laufenden Töne"""

def volume(volume: int):
    """Stelle die Standardlautstärke ein"""
