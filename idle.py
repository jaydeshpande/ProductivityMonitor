# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:32:02 2016

@author: Jaydeep
"""
import platform

if (platform.system()=='Darwin'):
	from Quartz.CoreGraphics import *
 
	# From /System/Library/Frameworks/IOKit.framework/Versions/A/Headers/hidsystem/IOLLEvent.h
	NX_ALLEVENTS = int(4294967295)  # 32-bits, all on.

 
	def get_idle_duration():
		"""Get number of seconds since last user input"""
		idle = CGEventSourceSecondsSinceLastEventType(1, NX_ALLEVENTS)
		return idle/1000.0

		
elif (platform.system()=='Windows'):
	from ctypes import Structure, windll, c_uint, sizeof, byref

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