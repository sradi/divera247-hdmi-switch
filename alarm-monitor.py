#! /usr/bin/python

import os
import time
import configparser
import divera
import hdmi_cec

os.system("DISPLAY=:0 chromium-browser --kiosk www.heise.de &")

config = configparser.ConfigParser()
config.read('/home/pi/divera.ini')

#Testeinheit
#ACCESS_KEY = "Cm81ukIkHhutHHZ42qC5Tz3cROZOqq3_BB9f0t3e8Cgr1Hry61k3MrO2lIvQjMBX"
#FF Bispinen Ortswehr Bispingen
ACCESS_KEY=config['Divera']['accessKey']

einheit = divera.Divera(ACCESS_KEY)
hdmiDevice0 = hdmi_cec.HdmiCec(0)

while True:
    hasOpenAlarms = einheit.has_open_alarms()
    if hasOpenAlarms:
        hdmiDevice0.on()
    else:
        hdmiDevice0.standby()
    time.sleep(120)
