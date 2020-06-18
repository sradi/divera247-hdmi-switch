# diver247-hdmi-switch
Skript, um bei aktiven Divera 24/7-Alarmen per HDMI-CEC einen Monitor einzuschalten.

## Installation
- bootstrap/install_ansible.sh als root ausführen.
- bootstrap/bootstrap.sh ausführen

## Start des Alarm-Monitors
- sudo su - divera
- screen <pfadZumRepository>/alarm-monitor.py
- Ctrl+A Ctrl+D
- (monitor-Prozess wieder in den Vordergrund holen: screen -r)