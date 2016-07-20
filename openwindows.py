# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:11:31 2016

@author: Jaydeep
"""
import platform

if (platform.system()=='Darwin'):
	from AppKit import NSWorkspace
	import time

	def findwindow():
		active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
		return active_app_name

elif (platform.system()=='Windows'):
	import win32gui
	w=win32gui
	def findwindow():
		openwindow = w.GetWindowText (w.GetForegroundWindow())
		return openwindow