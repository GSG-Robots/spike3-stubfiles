def data(port: int) -> tuple[int, ...]:
    """Ruf die LPF-2-Rohdaten von einem Gerät ab.
    
    :param port: Port des Color Sensors (:py:mod:`hub.port`)
    """
    
def id(port: int) -> int:
    """Ruf die Gerätekennung eines Geräts ab. Jedes Gerät hat eine Kennung (ID), die auf seinem Typ basiert.
    
    :param port: Port des Color Sensors (:py:mod:`hub.port`)
    """
    
def get_duty_cycle(port: int) -> int:
    """Ruf den Arbeitszyklus für ein Gerät ab.
    
    :param port: Port des Color Sensors (:py:mod:`hub.port`)
    
    :return: 0 bis 10000
    """
    
def set_duty_cycle(port: int, duty_cylce: int):
    """Stellt den Arbeitszyklus an einem Gerät ein.
    
    :param port: Port des Color Sensors (:py:mod:`hub.port`)
    :param duty_cycle: Bereich 0 bis 10000
    """
    
def ready(port: int) -> bool:
    """Gibt an, ob das Gerät initialisiert und bereit zur Verwendung ist.
    
    :param port: Port des Color Sensors (:py:mod:`hub.port`)
    """