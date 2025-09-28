"""
This is program generates a GUI for a simple calculator.
The calculator functions just as a normal calculator 
would the user just has to click the buttons.
"""

# Import tkinter
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Test window title")
# Set geometry of window (width x height)
root.geometry('500x400')

# adding a label to the root window
label = Label(root, text = "Hello world!")
label.grid()

# function to display text when the button is clicked

def testFunction():
    label.configure(text = "Goodbye world")

# actual button widget
button = Button(root, text = "Press here",
                fg="red", bg="black", command = testFunction)
# set button grid
button.grid(column=1, row=0)

# Execute Tkinter
root.mainloop() # endless loop to make the window run till we close it