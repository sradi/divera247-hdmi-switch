#! /usr/bin/python

import requests
import json

class Divera:

    API_BASE_URL = "https://www.divera247.com/api/v2"

    def __init__(self, accessKey):
        self._accessKey = accessKey

    def has_open_alarms(self):
        alarmsUrl = Divera.API_BASE_URL + "/alarms"

        # sending get request and saving the response as response object
        r = requests.get(url=alarmsUrl, params={'accesskey': self._accessKey})
        if r.status_code == 200:
            f = open("openAlarm_unformatted.json", "r")
            deserializedJson = json.loads(f.read())
            f.close()
            #print(r.json())
            #deserializedJson = r.json()
            allAlarms = deserializedJson["data"]["items"]

            if not type(allAlarms) is dict:
                # API liefert {u'data': {u'items': [], u'sorting': []}, u'ucr': 197008, u'success': True}...
                # wenn keine offenen Alarme existieren. items... leere Liste. Ansonsten ist es ein dict
                print("No open alarms (items was not of type 'dict'). Returned json: ", r.json())
                return False

            # treat allAlarms as dict
            for a in allAlarms.values():
                if a["closed"] == False:
                    return True
            return False
        else:
            print("Error requesting GET '", alarmsUrl, "'. Status code: ", r.status_code)
