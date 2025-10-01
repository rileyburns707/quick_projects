"""
calculator_gui.py
-----------------
This is program runs a calculator gui. It functions as a normal
simple calculator would.
"""

"""
Section 1: 'Backend'
In this section I set up Tkinter and the functions
"""
# Import tkinter
from tkinter import *

root = Tk()
root.title("Super awesome calculator")
root.geometry("350x400")

BUTTON_NUMBER_FONT = ("Helvetica", 20, "bold") # Font name, Font size
BUTTON_CONTROL_FONT = ("Helvetica", 20, "bold")
DISPLAY_FONT = ("Helvetica", 24, "bold")

# Functions for when buttons are clicked
def equals_clicked():
    """
    If equals is clicked then the string in the viewing bar is converted
    to a float and the equation is done. The output of the equation is
    converted back to a string and displayed in the viewing bar.

    Edge cases
    - Dividing by 0 shows 'Undefined'
    """
    try:
        ans = eval(viewing_bar.get())
        viewing_bar.delete(0, END)  # delete curr_display
        viewing_bar.insert(0, ans) 
    except ZeroDivisionError:
        viewing_bar.delete(0, END)
        viewing_bar.insert(0, "Undefined")
    except:                                    # General error catch
        viewing_bar.delete(0, END)
        viewing_bar.insert(0, "Error")

def clear_clicked():
    """
    This clears all the text in the viewing bar
    """
    viewing_bar.delete(0, END) 

def clicked(button_value):
    """
    If a button is clicked then the text is appended to a string and
    the string is displayed in the viewing bar
    """
    curr_display = viewing_bar.get()     # returns a string
    new_display = curr_display + str(button_value)
    viewing_bar.delete(0, END)  # delete curr_display
    viewing_bar.insert(0, new_display)      
    
# ---------------------------------------------------------------------------------
"""
Section 2: 'Frontend'
In this section I establish buttons and define the UI
"""
# Column configuration
viewing_bar = Entry(root, font=DISPLAY_FONT)
viewing_bar.grid(row=0, column=0, columnspan=4, sticky="nswe", padx=0, pady=0)
for i in range(4):
    root.grid_columnconfigure(i, weight = 1)

# Row configuration
for i in range(6):
    root.grid_rowconfigure(i, weight = 1)

# Control Buttons
# equals_button = Button(root, text="=", fg="orange", command=equals_clicked, font=BUTTON_CONTROL_FONT)

equals_button = Button(root, text="=", fg="orange", command=equals_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
clear_button = Button(root, text="C", fg="orange", command=clear_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
division_button = Button(root, text="/", fg="orange", command=lambda: clicked('/'), font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
multiplication_button = Button(root, text="*", fg="orange", command=lambda: clicked('*'), font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
subtraction_button = Button(root, text="-", fg="orange", command=lambda: clicked('-'), font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
addition_button = Button(root, text="+", fg="orange", command=lambda: clicked('+'), font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
decimal_button = Button(root, text=".", fg="orange", command=lambda: clicked('.'), font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)

# Number Buttons
zero = Button(root, text="0", fg="blue", command=lambda: clicked('0'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
one = Button(root, text="1", fg="blue", command=lambda: clicked('1'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
two = Button(root, text="2", fg="blue", command=lambda: clicked('2'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
three = Button(root, text="3", fg="blue", command=lambda: clicked('3'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
four = Button(root, text="4", fg="blue", command=lambda: clicked('4'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
five = Button(root, text="5", fg="blue", command=lambda: clicked('5'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
six = Button(root, text="6", fg="blue", command=lambda: clicked('6'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
seven = Button(root, text="7", fg="blue", command=lambda: clicked('7'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
eight = Button(root, text="8", fg="blue", command=lambda: clicked('8'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)
nine = Button(root, text="9", fg="blue", command=lambda: clicked('9'), font=BUTTON_NUMBER_FONT, bd=0, highlightthickness=2)

# Control Button Locations
clear_button.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=0, pady=0)
division_button.grid(row=1, column=3, sticky="nswe", padx=0, pady=0)
multiplication_button.grid(row=2, column=3, sticky="nswe", padx=0, pady=0)
subtraction_button.grid(row=3, column=3, sticky="wnswee", padx=0, pady=0)
addition_button.grid(row=4, column=3, sticky="nswe", padx=0, pady=0)
decimal_button.grid(row=5, column=2, sticky="nswe", padx=0, pady=0)
equals_button.grid(row=5, column=3, sticky="nswe", padx=0, pady=0)

# Number Button Locations
zero.grid(row=5, column=0, columnspan=2, sticky="nswe", padx=0, pady=0)
one.grid(row=4, column=0, sticky="wnswee", padx=0, pady=0)
two.grid(row=4, column=1, sticky="nswe", padx=0, pady=0)
three.grid(row=4, column=2, sticky="nswe", padx=0, pady=0)
four.grid(row=3, column=0, sticky="nswe", padx=0, pady=0)
five.grid(row=3, column=1, sticky="nswe", padx=0, pady=0)
six.grid(row=3, column=2, sticky="nswe", padx=0, pady=0)
seven.grid(row=2, column=0, sticky="nswe", padx=0, pady=0)
eight.grid(row=2, column=1, sticky="nswe", padx=0, pady=0)
nine.grid(row=2, column=2, sticky="nswe", padx=0, pady=0)

# Execute Tkinter
root.mainloop()  # endless loop to make the window run till we close it