import tkinter
import random
from tkinter import *

root = tkinter.Tk()
root.geometry('750x550')
root.title('Roll Dice')

label = tkinter.Label(root, text='', font=('Helvetica', 260))


def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button = tkinter.Button(root, text='roll dice', foreground='blue', command=roll_dice)
button.place(x=325,y=10)
root.mainloop()