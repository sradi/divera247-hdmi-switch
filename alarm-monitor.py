#! /usr/bin/python

import time
import configparser
import divera
import hdmi_cec

config = configparser.ConfigParser()
config.read('/home/divera/divera.ini')

#Testeinheit
#ACCESS_KEY = "Cm81ukIkHhutHHZ42qC5Tz3cROZOqq3_BB9f0t3e8Cgr1Hry61k3MrO2lIvQjMBX"
#FF Bispinen Ortswehr Bispingen
ACCESS_KEY=config['Divera']['accessKey']

einheit = divera.Divera(ACCESS_KEY)
hdmiDevice0 = hdmi_cec.HdmiCec(0)

hasOpenAlarms = einheit.has_open_alarms()
print("Open alarms? ", hasOpenAlarms)

while True:
    if hasOpenAlarms:
        hdmiDevice0.on()
    else:
        hdmiDevice0.standby()
    time.sleep(180)
