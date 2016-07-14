# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:06:50 2016

@author: Jaydeep Deshpande
"""
# this part is to fix the encoding issue with pandas export
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
# do not edit anything above this line

# code for productivity tracking 
import time # required for putting the code to sleep
import idle # required to find the idle time 
import gettimestamp # required to find current clock state
import openwindows as ow # required to find current active window
import pandas as pd
id = 0 ## start idle time just to get into the loop, loop should never end    
df = pd.DataFrame(columns=['month','date','hour','minute','second','active'])
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
#df.columns=['', '', '','', '', '','', '', '',]
while (id<15):
    A = ow.findwindow()
    T = gettimestamp.gettime()
    Q = [[T[1],T[2],T[3],T[4],T[5],A]]
    df = df.append(pd.DataFrame(Q, columns=['month','date','hour','minute','second','active']), ignore_index=True)
    df.to_excel(writer, sheet_name='Sheet1')    
    time.sleep(1)
    id = idle.get_idle_duration()

print 'EndRun'
writer.save()