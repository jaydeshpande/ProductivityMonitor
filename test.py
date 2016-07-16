# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:49:22 2016

@author: Jaydeep
"""

from AppKit import NSWorkspace
active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
print active_app_name