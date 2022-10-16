import tkinter
import random
from tkinter import *

root = tkinter.Tk()
root.geometry('750x550')
root.title('Dobbelsteen Emjee')

Namen = ["Ad", "Boaz", "Remi", "William"]
label = tkinter.Label(root, text='', font=('Helvetica', 260))

label1 = tkinter.Label(root, text='', font=('Helvetica', 100))
label1.place(x=70,y=50)

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
def genereer_namen():
    label1.configure(text=f'{random.choice(Namen)}')
    label1.pack()

button = tkinter.Button(root, text='Gooien', foreground='blue', command=lambda:[roll_dice(), genereer_namen()])
button.place(x=820,y=10)
button.pack()
root.mainloop()
