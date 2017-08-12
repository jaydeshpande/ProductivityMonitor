# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:32:02 2016

@author: Jaydeep
"""
import platform
from Quartz.CoreGraphics import *


def get_idle_duration():

    if (platform.system()=='Darwin'):
        NX_ALLEVENTS = int(4294967295)  # 32-bits, all on.
        idle = CGEventSourceSecondsSinceLastEventType(1, NX_ALLEVENTS)
        return round(idle,0)

		
    elif (platform.system()=='Windows'):
        from ctypes import Structure, windll, c_uint, sizeof, byref

        class LASTINPUTINFO(Structure):
            _fields_ = [
                ('cbSize', c_uint),
                ('dwTime', c_uint),
            ]
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return round(millis / 1000.0, 0)

if __name__ == "__main__":
    while (1):
        print (get_idle_duration())