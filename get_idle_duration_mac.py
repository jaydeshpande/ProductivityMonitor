
from Quartz.CoreGraphics import *
 
# From /System/Library/Frameworks/IOKit.framework/Versions/A/Headers/hidsystem/IOLLEvent.h
NX_ALLEVENTS = int(4294967295)  # 32-bits, all on.

 
def getIdleTime():
    """Get number of seconds since last user input"""
    idle = CGEventSourceSecondsSinceLastEventType(1, NX_ALLEVENTS)
    return idle

i=0;
while (i<1):
	idle = getIdleTime()
	print idle