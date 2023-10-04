from tkinter import *
import calendar
import tkinter
from tkinter import messagebox


def Whenpressed():
    date = int(textbox2.get())
    global text
    text = calendar.calendar(date)
    l1=Label(root,text= text,bg = "white", font=("Consolas 8 bold"))
    l1.pack()

root = Tk()
root.geometry("550x600")
root.configure(background = "light gray")
root.title("Calendar")
root.configure(background = "white")
label1 = Label(root,text="Calendar",bg= "dark gray", font=("times",28,"bold"))
label1.pack()
textbox2 = tkinter.Entry(root,fg="black",bg="white",width=7,font=("Ariel",8))
button1 = tkinter.Button(root,text="Get year",fg="black",bg="AntiqueWhite2",command = Whenpressed)
textbox2.pack()
button1.pack()




root.mainloop()
