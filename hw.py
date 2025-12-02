from tkinter import *
import tkinter.font as font
from time import strftime
import random

root = Tk()
root.title("Clock + Effect")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

timelabel = Label(root, font=("calibri", 60, "bold"), background="black", foreground="white")
timelabel.pack(fill="both", expand=True)

def update():
    current_time = strftime("%H:%M:%S %p")
    timelabel.config(text=current_time)
    new_color = random.choice(colors)
    timelabel.config(background=new_color)
    timelabel.after(1000, update)

update()
root.mainloop()
