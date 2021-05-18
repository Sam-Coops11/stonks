##
# stonks_v3.py
# Sam Cooper
# 19/5/21
# refactoring our program to use a dict. of dicts.

def add_stonk(dictionary, key, value):
    """
    Add a new stonk to the dict.
    """
    dictionary[key] = value
    return dictionary


def add_ticker():
    """
    Ask user for a stock ticker and error check
    """
    while True:
        try:
            ticker = input("Enter the stock ticker: ")
            ticker = int(ticker)
            print("A stock ticker cannot contain numbers!")
        except:
            break

    return ticker


def add_price():
    """
    Ask user for the price of the stock and err. check
    """
    MAX_PRICE = 100000
    MIN_PRICE = 0
    while True:
        try:
            price = float(input("Enter the current stock price: "))
            if price < MIN_PRICE or price > MAX_PRICE:
                print('The price is out of range')
            else:
                break
        except:
            print("Not a valid input")

    return price


def add_full_name():
    """
    """
    full_name = input("Enter the full name of the stonk: ")

    return full_name


def add_industry():
    """
    """
    industry = input("Enter the industry of the stonk: ")

    return industry
# main routine
if __name__ in "__main__":
    stonks = {
        "GME": {
            "price":180.67,
            "prev_closing_price":160.70,
            "full_name":"GameStop"
            },
        "AAPL" : {
            "price":124.85,
            "prev_closing_price":125.66,
            "industry":"Technology"
            }
        }
