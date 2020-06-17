#! /usr/bin/python

import time
import divera
import hdmi_cec

#Testeinheit
ACCESS_KEY = "Cm81ukIkHhutHHZ42qC5Tz3cROZOqq3_BB9f0t3e8Cgr1Hry61k3MrO2lIvQjMBX"
#FF Bispinen Ortswehr Bispingen
#ACCESS_KEY=

diveraTesteinheit = divera.Divera(ACCESS_KEY)
hdmiDevice0 = hdmi_cec.HdmiCec(0)

hasOpenAlarms = diveraTesteinheit.has_open_alarms()
print("Open alarms? ", hasOpenAlarms)

while True:
    if hasOpenAlarms:
        hdmiDevice0.on()
    else:
        hdmiDevice0.standby()
    time.sleep(180)
