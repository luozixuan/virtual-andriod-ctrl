# -*- coding: utf-8 -*-
import os
import time


class adbClient:
    def __init__(self):
        print "new adb client"
    def set_command(self,command):
        print command
        #ret = os.system(command)
        fd = os.popen(command)
        time.sleep(2)
        retstring = fd.read()
        return retstring
    def get_screenshot(self):
         imagpath = os.path.join(os.getcwd(),"ss.png")
         if True == os.path.exists(imagpath):
             os.remove(imagpath)
         command = "adb shell screencap -p /sdcard/ss.png"
         self.set_command(command)
         #time.sleep(3)
         command = "adb pull /sdcard/ss.png " + os.getcwd()
         self.set_command(command)
         return imagpath
    def connect_to_virtualmachine(self):
        command = "adb connect 127.0.0.1:7555"
        reply = self.set_command(command)
        if reply.find("unable to") != -1:
            print "Can't find virtual devices"
            return False
        else:
            print "connected!!"
            return True
    def open_web_with_browser(self,web):
        command = "adb shell am start -a android.intent.action.VIEW -d " + web
        self.set_command(command)
    def swipe_action(self,x0,y0,x1,y1,delay):
        command = "adb shell input touchscreen swipe "+ str(x0)+" "+str(y0) +" " +\
                str(x1)+" "+str(y1)+" "+str(delay)
        self.set_command(command)
    def getdevices(self):
        command = "adb devices"
        return self.set_command(command)
    def click_action(self,x,y):
        command = "adb shell input touchscreen tap " + str(x) + " " + str(y)
        self.set_command(command)
~                                       
