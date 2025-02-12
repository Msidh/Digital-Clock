from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")


# x stores systems time 
def showtime():
    x = strftime("%H:%M:%S %p")
    time_label.config(text = x)
    time_label.after(1000,showtime)



#Time label
time_label = Label(window, text = "", font = ("calibri",40,"bold"), background = "black", foreground = "white")
time_label.grid(row = 0 ,column = 0)



showtime()


window.mainloop()