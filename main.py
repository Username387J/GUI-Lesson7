#Digital Clock
from tkinter import *
from time import strftime
root=Tk()
root.title("Live Clock")

timelabel=Label(root,font=('calibri',40,'bold'),background='grey',foreground='white')
timelabel.pack()

def time():
    string=strftime('%H:%M:%S:%p')
    timelabel.config(text=string)
    timelabel.after(1000,time)

time()


root.mainloop()