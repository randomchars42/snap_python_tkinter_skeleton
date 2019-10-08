#!/usr/bin/env python3

from tkinter import *
 
class PhotoPy:
    def run(self):
        print("initialising tk: window = Tk()")
        window = Tk()
        print("done")
        print("adding window title: window.title(TEXT)")
        window.title("TKinter Window")
        print("done")
        print("creating a label: label = Label(window)")
        label = Label(window, text="Hello World!")
        print("done")
        print("adding label to the grid: label.grid()")
        label.grid(column=0, row=0)
        print("done")
        print("go: window.mainloop()")
        window.mainloop()
        print("running")
