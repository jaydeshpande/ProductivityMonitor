# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:06:50 2016

@author: USJADES
"""

# code for productivity tracking 
import time
from ctypes import Structure, windll, c_uint, sizeof, byref
import win32gui
w=win32gui
def findwindow():
    openwindow = w.GetWindowText (w.GetForegroundWindow())
    return openwindow
# http://stackoverflow.com/questions/911856/detecting-idle-time-in-python

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
 
def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

idle = 0    
while (idle<10):
    idle = get_idle_duration()
    if idle==0:
        print findwindow()
        time.sleep(5)
print 'endrun'