import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    """This class encapsulates the main window"""
    def __init__(self):
        # main setup
        super().__init__()
        self.title("London Darwin Time Converter") # name window
        self.geometry('1000x400') # change window size

        # widgets

        # run
        self.mainloop()

