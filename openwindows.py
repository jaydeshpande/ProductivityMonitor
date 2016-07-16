# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:11:31 2016

@author: Jaydeep
"""

import win32gui
w=win32gui
def findwindow():
    openwindow = w.GetWindowText (w.GetForegroundWindow())
    return openwindow