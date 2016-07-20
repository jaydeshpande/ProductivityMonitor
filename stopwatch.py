import random
import math
#import turtle
import time
import Tkinter
from Tkinter import *

root = Tkinter.Tk()

# running = False

class Stopwatch(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        self.running = False
        self.timer = [0,0,0]    # [minutes ,seconds, centiseconds]
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.update_time()

    def widgets(self):
        self.timeFrame = LabelFrame(root, text='Time Frame', width=1200)
        self.timeFrame.grid(row=0,column=0, sticky=W)

        self.resetButton = Button(self.timeFrame, text='Reset', command=self.resetTime)
        self.resetButton.grid(row=2,column=1)

        self.pauseButton = Button(self.timeFrame, text='Pause', command=self.pause)
        self.pauseButton.grid(row=1,column=1)

        self.startButton = Button(self.timeFrame, text='Start', command=self.start)
        self.startButton.grid(row=0,column=1)

        self.show = Label(self.timeFrame, text='00:00:00', font=('Helvetica', 30))
        self.show.grid(row=0, column=0)

        # Quit Button
        self.quit = Button(self.timeFrame, text='QUIT', command=self.quit)
        self.quit.grid(row=3, column=1)


    def update_time(self):

        if (self.running == True):      #Clock is running

            self.timer[2] += 1

            if (self.timer[2] >= 100):  #100 centiseconds --> 1 second
                self.timer[2] = 0
                self.timer[1] += 1      #add 1 second

            if (self.timer[1] >= 60):   #60 seconds --> 1 minute
                self.timer[0] += 1
                self.timer[1] = 0

            self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
            self.show.config(text=self.timeString)
        root.after(10, self.update_time)


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