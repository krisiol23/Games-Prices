#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
import os


window = tkinter. Tk()
window.title("Games_prices")

label = Label(window, text = "Game link")
label.grid(row = 0, column = 0)

textbox = Entry(window)
textbox.grid(row = 1, column = 0, padx = 5, pady = 10)
button = Button(window, text="ADD")
button.grid(row = 1, column  = 1)

combobox = ttk.Combobox(window, values = ["Epic Games", "Steam", "Origin", "Uplay"], state = "readonly", width = 17)
combobox.grid(row = 2, column = 0)


button1 = Button(window, text="ACCEPT")
button1.grid(row = 3, column = 0, pady = 10)

path = os.getcwd()
parent = os.path.dirname(path) 
new = os.chdir("../webscrappers") 

with open("data.txt") as f:
	label1 = Label(window, text = f.read())
	label1.grid(row = 4, column = 1)


window.geometry("400x400")
window.mainloop()
