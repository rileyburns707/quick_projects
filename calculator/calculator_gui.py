"""
calculator_gui.py
-----------------
This is program runs a calculator gui. It functions as a normal
simple calculator would.
"""

# Import tkinter
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Super awesome calculator")
root.geometry("350x400")

# Functions for when buttons are clicked
def equals_clicked():
    pass

def clicked():
    pass

# Using Entry widget as the viewing bar
viewing_bar = ttk.Entry(root)
viewing_bar.grid(row=0, column=0, columnspan=4, sticky="we")
for i in range(4):
    root.grid_columnconfigure(i, weight = 1)


# Buttons
equals_button = ttk.Button(root, text="=", fg="red", bg = "orange", highlightbackground="orange", command=equals_clicked)
equals_button.grid(row=1, column=1)




# Execute Tkinter
root.mainloop() # endless loop to make the window run till we close it