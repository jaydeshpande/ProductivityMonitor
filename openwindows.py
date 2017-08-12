# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:11:31 2016

@author: Jaydeep
"""
import platform
import time
from AppKit import NSWorkspace
#import win32gui


def getapp():
    print (platform.system())
    if (platform.system()=='Darwin'):
        def findwindow():
            active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
            return active_app_name

    elif (platform.system()=='Windows'):
        w=win32gui
        def findwindow():
            openwindow = w.GetWindowText (w.GetForegroundWindow())
            return openwindow

if __name__ == '__main__':
    i=0
    while(i<1):
        print (getapp())
        time.sleep(2)