# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:59:18 2016

@author: USJADES
"""
import Tkinter as tk

class app_tk(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        button = tk.Button(self,text=u"Start",command=self.OnButtonClick)
        button.pack()
        button = tk.Button(self,text=u"Stop",command=self.destroy)
        button.pack()


    def OnButtonClick(self):
        while(1):        
            print "code runs"

if __name__ == "__main__":
    app = app_tk(None)
    app.title('my application')
    app.mainloop()
    

    