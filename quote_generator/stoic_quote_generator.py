"""
stoic_quote_generator.py
------------------------
This program runs a simple GUI that generators a random quote
from a stoic. It calls an API to get the quotes.
"""

import requests
from tkinter import *

"""
class stoicQuotes():
    def __init__(self, root):
        self.root = root
        self.root.title("Stoic quote generator")

stoicQuotes(root)
root.mainloop()  # endless loop to make the window run till we close it
"""

root = Tk()
root.title("Stoic quote generator")
root.geometry("500x200")

BUTTON_CONTROL_FONT = ("Helvetica", 20, "bold")
PROMPT_FONT = ("Helvetica", 22, "bold")
QUOTE_FONT = ("Helvetica", 14, "bold")


def get_quote():
    """
    This function requests the quote from API and prints the quote and author if a 
    successful connection is made. If not, an error message shows.
    """
    url = "https://stoic.tekloon.net/stoic-quote"   # API endpoint url

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # Convert JSON to Python dict
            data_info = data['data'] # get the author and quote from the data
            quote = Label(root, text=f"{data_info['quote']}\n        - {data_info['author']}", font=QUOTE_FONT)
            quote.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)
            return data_info            
        else:
            print("Error: " + str(response.status_code))

    except requests.exceptions.RequestException as error:
        print("Error: " + str(error))
        return None

def main():
    """
    This function runs the GUI that the quote will be in. There is a start, stop, and clear button
    """

    """
    Section 1: 'Backend'
    In this section I set up Tkinter and the functions
    """

    def yes_clicked():
        # Clears the prompt and buttons. Calls the API and prints a quote.
        prompt.grid_forget()
        yes.grid_forget()
        no.grid_forget()
        get_quote()

    def no_clicked():
        # Clears the prompt and buttons and shows the no worries method
        pass

    def refresh():
        # Clears any quote and shows the prompt with yes and no again
        # quote.grid_forget()
        prompt.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)
        pass

    # ---------------------------------------------------------------------------------
    """
    Section 2: 'Frontend'
    In this section I establish buttons and define the UI
    """
    # Column configuration
    for i in range(6):
        root.grid_columnconfigure(i, weight = 1)

    # Row configuration
    for i in range(6):
        root.grid_rowconfigure(i, weight = 1)

    # Initial prompt
    prompt = Label(root, text = "Would you like a quote?", font=PROMPT_FONT)
    prompt.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)

    # Control Buttons
    yes = Button(root, text="Yes", fg="green", command=yes_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
    no = Button(root, text="No", fg="red", command=no_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
    refresh_button = Button(root, text="🔄", command=refresh, bd=0, highlightthickness=2)

    # Control button location
    yes.grid(row=2, column=3, padx=2, pady=5)
    no.grid(row=2, column=4, padx=2, pady=5)
    refresh_button.grid(row=0, column=6, sticky="ne", padx=0, pady=0)

    # Execute Tkinter
    root.mainloop()  # endless loop to make the window run till we close it    

if __name__ == '__main__':
    main()