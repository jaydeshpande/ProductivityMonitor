# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:39:54 2016

@author: Jaydeep Deshpande
"""

import time
import Tkinter
from Tkinter import *
import sys  
import matplotlib.pyplot as plt
reload(sys)  
sys.setdefaultencoding('utf8')
# do not edit anything above this line

# code for productivity tracking 
import time # required for putting the code to sleep
import idle # required to find the idle time 
import gettimestamp # required to find current clock state
import openwindows as ow # required to find current active window
import pandas as pd
root = Tkinter.Tk()

id = 0 ## start idle time just to get into the loop, loop should never end    
global df
today = gettimestamp.gettime()
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
# running = False

class Stopwatch(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        self.running = False
        self.timer = [0,0,0]    # [minutes ,seconds, centiseconds]
        self.id = 0             # idle time at the initial instance
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.update_time()
        self.df = pd.DataFrame(columns=['month','date','hour','minute','second','window','status'])

    def widgets(self):
        self.timeFrame = LabelFrame(root, text='Time Running', width=1200)
        self.timeFrame.grid(row=0,column=0, sticky=W)

        #self.resetButton = Button(self.timeFrame, text='Reset', command=self.resetTime)
        #self.resetButton.grid(row=2,column=1)

        #self.pauseButton = Button(self.timeFrame, text='Pause', command=self.pause)
        #self.pauseButton.grid(row=1,column=1)

        self.startButton = Button(self.timeFrame, text='Start', command=self.start)
        self.startButton.grid(row=0,column=1)

        self.show = Label(self.timeFrame, text='00:00:00', font=('Helvetica', 30))
        self.show.grid(row=1, column=0)

        # Quit Button
        self.quit = Button(self.timeFrame, text='Stop', command=self.quit)
        self.quit.grid(row=2, column=1)


    def update_time(self):
        global df
        if (self.running == True):      #Clock is running

            self.timer[2] += 1
            self.id = idle.get_idle_duration()
            if (self.id<300):           # idle duration 5 minutes 
                A = ow.findwindow()
                T = gettimestamp.gettime()
                Q = [[T[1],T[2],T[3],T[4],T[5],A, 'Active']]
                self.df = self.df.append(pd.DataFrame(Q, columns=['month','date','hour','minute','second','window','status']), ignore_index=True)
                self.df.to_excel(writer, sheet_name='Sheet1')
            else:
                A = ow.findwindow()
                T = gettimestamp.gettime()
                Q = [[T[1],T[2],T[3],T[4],T[5],A, 'Idle']]
                self.df = self.df.append(pd.DataFrame(Q, columns=['month','date','hour','minute','second','window','status']), ignore_index=True)
                self.df.to_excel(writer, sheet_name='Sheet1')
                
            if (self.timer[2] >= 100):  #100 centiseconds --> 1 second
                self.timer[2] = 0
                self.timer[1] += 1      #add 1 second

            if (self.timer[1] >= 60):   #60 seconds --> 1 minute
                self.timer[0] += 1
                self.timer[1] = 0

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
            self.show.config(text=self.timeString)
        root.after(1000, self.update_time)


    def start(self):            #Start the clock
        self.running = True
        print 'Clock Running...'

    def pause(self):            #Pause the clock
        self.running = False
        print 'Clock Paused'    

    def resetTime(self):        #Reset the clock
        self.running = False
        self.timer = [0,0,0]
        print 'Clock is Reset'  
        self.show.config(text='00:00:00')

    def quit(self):             #Quit the program
        root.destroy()
        


watch = Stopwatch(root)

root.mainloop()