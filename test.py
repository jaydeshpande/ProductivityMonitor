# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:49:22 2016

@author: USJADES
"""

import win32gui
w=win32gui
test = w.GetWindowText (w.GetForegroundWindow())
print test 