#! /bin/bash

# HDMI Devices scannen
#echo 'scan' | cec-client -s -d 1

# HDMI Device ein
#echo 'on 0' | cec-client -s -d 1

# HDMI Device aus
#echo 'standby 0' | cec-client -s -d 1

#Testeinheit
ACCESS_KEY=Cm81ukIkHhutHHZ42qC5Tz3cROZOqq3_BB9f0t3e8Cgr1Hry61k3MrO2lIvQjMBX

#FF Bispinen Ortswehr Bispingen
#ACCESS_KEY=

#GET_ALARMS_CURL="curl -X GET \"https://www.divera247.com/api/v2/alarms?accesskey=${ACCESS_KEY}\" -H  \"accept: application/json\""
GET_ALARMS_CURL="curl -X GET "https://www.divera247.com/api/v2/alarms?accesskey=${ACCESS_KEY}""
$(${GET_ALARMS_CURL})

#hasOpenAlarms=$(${GET_ALARMS_CURL} | jq '.data.items | .[] | select(.closed==false)')

#echo "Offene Alarme? ${hasOpenAlarms}"

# Chromium in full-screen oder kiosk mode: https://www.raspberrypi.org/forums/viewtopic.php?t=205426


