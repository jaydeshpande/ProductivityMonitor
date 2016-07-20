from AppKit import NSWorkspace
import time

def getapp():
	active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
	return active_app_name


i=0
while(i<1):
	print getapp()
	time.sleep(2)