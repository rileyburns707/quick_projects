"""
sandbox.py
----------
This is a file for me to try different API calls, errors,
excepts, and test APIs in general
"""

import requests

def get_quote():
    url = "https://stoic.tekloon.net/stoic-quote"   # API endpoint url

    try:
        response = requests.get(url)

        if response.status_code == 200:
            # print the quote
            data = response.json()
            quote_info = data["data"]
            print(f"'{quote_info['quote']}'\n       — {quote_info['author']}\n")
            return quote_info
        else:
            print("Error", response.status_code)
            return None
    
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def main():
    question = input("\nWould you like a Stoic quote (Y/N): ").upper()

    if question == "Y":
        print("Coming right up...\n")
        get_quote()
        
    else:
        print("No worries have a great day!\n")

if __name__ == '__main__':
    main()