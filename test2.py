import random
import time
from Tkinter import *


root = Tk()

w = Label(root, text="GAME")
w.pack()

frame = Frame(root, width=300, height=300)
frame.pack()

L1 = Label(root, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)

tiles_letter = ['a', 'b', 'c', 'd', 'e']

def add_letter():
    rand = random.choice(tiles_letter)
    tile_frame = Label(frame, text=rand)
    tile_frame.pack()
    root.after(500, add_letter)
    tiles_letter.remove(rand)  # remove that tile from list of tiles


root.after(0, add_letter)  # add_letter will run as soon as the mainloop starts.
root.mainloop()