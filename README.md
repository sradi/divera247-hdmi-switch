# diver247-hdmi-switch
Skript, um bei aktiven Divera 24/7-Alarmen per HDMI-CEC einen Monitor einzuschalten.

## Installation
- bootstrap/install_ansible.sh als root ausführen.
- bootstrap/bootstrap.sh ausführen

## Start des Alarm-Monitors
- Der Alarm-Monitor wird via Autostart ausgeführt (wenn kein Alarm aktiv ist, schaltet sich der Monitor direkt auf Standby)
- Manuell den Monitor einschalten (via SSH): `echo 'on 0' | cec-client -s -d 1`
- Manuell den Monitor ausschalten (via SSH): `echo 'standby 0' | cec-client -s -d 1`

### Manueller Start (im Vordergrund)
- `<pfadZumRepository>/alarm-monitor.py`

### Manueller Start (im Hintergrund)
- `screen <pfadZumRepository>/alarm-monitor.py`
- Ctrl+A Ctrl+D
- (monitor-Prozess wieder in den Vordergrund holen: `screen -r`)
