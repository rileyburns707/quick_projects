"""
stoic_quote_generator.py
------------------------
This program runs a simple GUI that generators a random quote
from a stoic. It calls an API to get the quotes.
"""
import requests
from tkinter import *

class stoicQuotes():
    def __init__(self, root):
        self.root = root
        self.root.title("Stoic quote generator")
        self.main()
        self.root.after(100, lambda: self.root.focus_force())

    def main(self):
        """
        This function sets up the the GUI layout by creating the buttons, the prompt, and the grid.
        """
        BUTTON_CONTROL_FONT = ("Helvetica", 20, "bold")
        PROMPT_FONT = ("Helvetica", 22, "bold")

        # Column configuration
        for i in range(6):
            root.grid_columnconfigure(i, weight = 1)

        # Row configuration
        for i in range(6):
            root.grid_rowconfigure(i, weight = 1)

        # Initial prompt
        self.prompt = Label(root, text = "Would you like a quote?", font=PROMPT_FONT)
        self.prompt.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)

        # Control Buttons
        self.yes = Button(root, text="Yes", fg="green", command=self.yes_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
        self.no = Button(root, text="No", fg="red", command=self.no_clicked, font=BUTTON_CONTROL_FONT, bd=0, highlightthickness=2)
        self.refresh_button = Button(root, text="🔄", command=self.refresh, bd=0, highlightthickness=2)

        # Control button location
        self.yes.grid(row=2, column=3, padx=2, pady=5)
        self.no.grid(row=2, column=4, padx=2, pady=5)
        self.refresh_button.grid(row=0, column=6, sticky="ne", padx=0, pady=0)

    def get_quote(self):
        """
        This function runs when the yes button is pressed. It requests the quote from the API 
        and prints the quote and author if a successful connection is made. If not, an 
        error message shows in the terminal.
        """
        QUOTE_FONT = ("Helvetica", 14, "bold")

        url = "https://stoic.tekloon.net/stoic-quote"   # API endpoint url
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json() # Convert JSON to Python dict
                data_info = data['data'] # get the author and quote from the data
                self.quote = Label(
                    root,
                    text=f"{data_info['quote']}\n        - {data_info['author']}",
                    font=QUOTE_FONT,
                    wraplength=400, 
                    justify="center"
                )
                self.quote.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)
                return data_info            
            else:
                print("Error: " + str(response.status_code))

        except requests.exceptions.RequestException as error:
            print("Error: " + str(error))
            return None
        
    def yes_clicked(self):
        """
        This function runs when the yes button is pressed. It clears the yes and no buttons 
        and the prompt, then calls the get_quote function to print the quote.
        """
        self.prompt.grid_forget()
        self.yes.grid_forget()
        self.no.grid_forget()
        self.get_quote()

    def no_clicked(self):
        """
        This function runs when the no button is pressed. This function clears the prompt, 
        yes button, and no button, then prints a no worries message.
        """
        NO_WORRIES_FONT = ("Helvetica", 22, "bold")

        self.prompt.grid_forget()
        self.yes.grid_forget()
        self.no.grid_forget()

        self.no_worries = Label(root, text=f"No worries, have a great day!", font=NO_WORRIES_FONT)
        self.no_worries.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)

    def refresh(self):
        """
        This function runs when the 🔄 button is pressed. It checks to see what is being
        displayed, and clears it all. It refeshes to the initial prompt, yes button, and 
        no button being displayed.
        """
        if hasattr(self, "prompt") and self.prompt.winfo_ismapped():
            self.prompt.grid_forget()

        if hasattr(self, "yes") and hasattr(self, "no"):
            if self.yes.winfo_ismapped() and self.no.winfo_ismapped():
                self.yes.grid_forget()
                self.no.grid_forget()

        if hasattr(self, "quote") and self.quote.winfo_ismapped():
            self.quote.grid_forget()

        if hasattr(self, "no_worries") and self.no_worries.winfo_ismapped():
            self.no_worries.grid_forget()
        
        self.prompt.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)
        self.yes.grid(row=2, column=3, padx=2, pady=5)
        self.no.grid(row=2, column=4, padx=2, pady=5)
        
root = Tk()
root.title("Stoic quote generator")
root.geometry("500x200")
stoicQuotes(root)
root.update()
root.mainloop()  # endless loop to make the window run till we close it