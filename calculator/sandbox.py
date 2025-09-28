"""
sandbox.py
----------
This is program is a sandbox for me to try different tkinter
commands and learning how it works.
"""

# Import tkinter
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# root window title and dimension
root.title("Test window title")
# Set geometry of window (width x height)
root.geometry('500x400')


# adding a menu bar in the root window
# new item in menu bar labelled as 'New'
# adding more items in the mneu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='Test')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


# adding a label to the root window
label = Label(root, text = "What is 5*5?")
label.grid()

# adding Entry field
text = Entry(root, width=8)
text.grid(column=1, row=0)

# function to display text when the button is clicked
def clicked():
    ans = "You answered: " + text.get()
    label.configure(text = ans)

# actual button widget
button = Button(root, text = "Press here",
                fg="blue", command = clicked)
# set button grid
button.grid(column=2, row=0)

# Execute Tkinter
root.mainloop() # endless loop to make the window run till we close it