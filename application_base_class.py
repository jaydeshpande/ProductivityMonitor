import platform
from datetime import datetime
from AppKit import NSWorkspace
import time
#from Quartz.CoreGraphics import *
#import win32gui

class application_properties:

    def __init__(self,name):
        self.name = name
        self.timeHistory = {}
        self.instances = 1
        self.update_time_objects()

    def update_time_objects(self):
        self.starttime = self.get_time_stamp()
        while (self.name == self.get_window_title()):
            self.currentTimeStampOnApplication = self.get_time_stamp()

            self.timeHistory[self.instances] = (self.name, self.starttime, self.currentTimeStampOnApplication,
                                                self.get_time_spent(self.starttime, self.currentTimeStampOnApplication))
            print (self.timeHistory[self.instances])
            time.sleep(2)
        self.instances += 1

    @staticmethod
    def get_window_title():
        if (platform.system() == 'Darwin'):
            active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
            return active_app_name
        else:
            openwindow = None
            # openwindow = win32gui.GetWindowText (w.GetForegroundWindow())
            # TODO developing this on Mac - to be tested on windows separately
            return openwindow

    @staticmethod
    def get_time_stamp():
        timestamp = datetime.now()
        return timestamp

    @staticmethod
    def get_time_spent(t1, t2):
        time_spent = t2 - t1
        return time_spent.seconds
    @staticmethod
    def get_idle_duration():
        if (platform.system() == 'Darwin'):
            NX_ALLEVENTS = int(4294967295)  # 32-bits, all on.
            idle = CGEventSourceSecondsSinceLastEventType(1, NX_ALLEVENTS)
            return idle / 1000.0

        else:
            from ctypes import Structure, windll, c_uint, sizeof, byref
            class LASTINPUTINFO(Structure):
                _fields_ = [('cbSize', c_uint),('dwTime', c_uint),]
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = sizeof(lastInputInfo)
            windll.user32.GetLastInputInfo(byref(lastInputInfo))
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0

if __name__ == "__main__":
    while(1):
        pass