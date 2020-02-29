#! /usr/bin/python

import os

class HdmiCec:

    def __init__(self, deviceNo):
        self.deviceNo = deviceNo

    def on(self):
        on_command = "echo 'on %d' | cec-client -s -d 1" % self.deviceNo
        print("Executing... ", on_command)
        os.system(on_command)

    def standby(self):
        standby_command = "echo 'standby %d' | cec-client -s -d 1" % self.deviceNo
        print("Executing...", standby_command)
        os.system(standby_command)