#! /usr/bin/python

import divera

#Testeinheit
ACCESS_KEY = "Cm81ukIkHhutHHZ42qC5Tz3cROZOqq3_BB9f0t3e8Cgr1Hry61k3MrO2lIvQjMBX"
#FF Bispinen Ortswehr Bispingen
#ACCESS_KEY=

d = divera.Divera(ACCESS_KEY)
print(d.has_open_alarms())
