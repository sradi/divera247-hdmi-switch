#! /usr/bin/python

import os

class HdmiCec:

    def __init__(self, deviceNo):
        self.deviceNo = deviceNo
        self.lastCommand = ""
        os.system("echo 'scan' | cec-client -s -d 1")

    def on(self):
        if self.lastCommand == "on":
            print "device ", self.deviceNo, " already on"
            return
        self.lastCommand = "on"
        on_command = "echo 'on %d' | cec-client -s -d 1" % self.deviceNo
        print("Executing... ", on_command)
        os.system(on_command)

    def standby(self):
        if self.lastCommand == "standby":
            print "device ", self.deviceNo, " already in standby"
            return
        self.lastCommand = "standby"
        standby_command = "echo 'standby %d' | cec-client -s -d 1" % self.deviceNo
        print("Executing...", standby_command)
        os.system(standby_command)
