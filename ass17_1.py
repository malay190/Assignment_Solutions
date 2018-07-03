#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.


import tkinter
from tkinter import *
import sys

def exit():
	print("Hello World!")
	sys.exit()
	
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)

label=Label(root,text='Hello World!')
label.pack()

b=Button(root,text="exit",bg='green',width=25,command=exit)
b.pack()

root.mainloop()
