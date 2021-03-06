#! /usr/bin/python

import requests
import json
import random

class Divera:

    API_BASE_URL = "https://www.divera247.com/api/v2"

    def __init__(self, accessKey):
        self._accessKey = accessKey

    def __get_json(self):
        alarmsUrl = Divera.API_BASE_URL + "/alarms"

        # sending get request and saving the response as response object
        r = requests.get(url=alarmsUrl, params={'accesskey': self._accessKey})
        if r.status_code == 200:
            #print(r.json())
            return r.json()
        else:
            print("Error requesting GET '", alarmsUrl, "'. Status code: ", r.status_code)
            return False

    def has_open_alarms(self):
        #return random.choice([True, False])

        deserializedJson = self.__get_json()
        allAlarms = deserializedJson["data"]["items"]

        if not type(allAlarms) is dict:
            # API liefert {u'data': {u'items': [], u'sorting': []}, u'ucr': 197008, u'success': True}...
            # wenn keine offenen Alarme existieren. items... leere Liste. Ansonsten ist es ein dict
            print "No open alarms (items was not of type 'dict'). Returned json: ", deserializedJson
            return False

        # treat allAlarms as dict
        for a in allAlarms.values():
            if a["closed"] == False:
                return True
        return False
        
