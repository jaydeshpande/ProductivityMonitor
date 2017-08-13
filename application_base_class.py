import platform
from datetime import datetime
from AppKit import NSWorkspace
import time
import idle
import csv
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
            idle_on_app = idle.get_idle_duration()
            if idle_on_app < 300:
                time.sleep(2)
            else:
                while idle.get_idle_duration() > 1:
                    time.sleep(2)
                break
        self.save_time_objects()
        self.instances += 1

    def save_time_objects(self):
        with open('timeHistory.csv', 'a') as csvfile:
            timestamp = str(datetime.today().date().month) + '/' + \
                        str(datetime.today().date().day) + '/' + str(datetime.today().date().year)
            fieldnames = ['timestamp', 'instance' , 'Application', 'timeHistory']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'timestamp': timestamp, 'instance': self.instances, 'Application': self.name,
                             'timeHistory':self.timeHistory[self.instances]})

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

if __name__ == "__main__":
    while(1):
        pass