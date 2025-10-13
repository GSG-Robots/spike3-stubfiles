# Spike V3 stubfiles

Inoffizielle Python stubfiles für die Spike V3 Python API.

Die Dateien haben die Dateiendung ``.py`` statt ``.pyi``, da Sphinx scheinbar keinen Support für ``.pyi``-Dateien bereitstellt.

## Completion

- [x] ``color``
- [x] ``color_matrix``
- [x] ``color_sensor``
- [x] ``device``
- [x] ``distance_sensor`` - Hat das wirklich die Funktionen von ``color_matrix``?
- [x] ``force_sensor``
- [ ] ``hub``
- [x] ``motor``
- [x] ``motor_pair``
- [x] ``orientation``
- [x] ``runloop``

Generell müssen alle Funktionen noch einmal auf Korrektheit überprüft werden,
da die (fehlerhafte) offizielle Dokumentation und nicht das tatsächliche Betriebssystem
zugrundegelegt wurde.
