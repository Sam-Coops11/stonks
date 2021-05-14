##
# stonks.py
# Sam Cooper
# 14/5/21
# Print and edit stocks


def add(dictionary):
    """
    Add to dictionary.
    """
    while True:
        try:
            key = input("What is the stonk: ")
            break
        except:
            print("Enter a valid answer")
            

    value = float(input("What is the stonk value: "))
    initial_price = value
    dictionary[key] = value
   
    return dictionary

# Modify from dictionary
def edit(dictionary):
    """
    Check if the key is in the dictionary
    then modify and return
    """
    PERCENT = 100
    percent_change = 0
    # Force a valid answer from user
    while True:
        try:
            key = str(input("What is the stonk to change: "))
            break
        except:
            print("Not a valid stonk")
    # check if the key is in dictionary
    if key in dictionary:
        # Change value
        value = float(input("Enter new stonk price: "))
        final_price = value
        value = dictrionary[key]
        percent_change = final_change / initial_change * PERCENT
    else:
        print("That stonk doesnt exist!")

    return dictionary, percent_change
        


# Delete from dictionary
def delete(dictionary):
    """
    """
    # Force a valid answer from user
    while True:
        try:
            key = str(input("What is the stonk to delete: "))
            break
        except:
            print("Not a valid stonk")

    # check if the key is in dictionary
    if key in dictionary:
        # delete value
        del dictionary[key]
    else:
        print("That stonk doesnt exist!")
        
    return dictionary


# Prints all entrys
def print_all(dictionary):
    """
    Print 
"""
    for key, value in sorted(dictionary.items()):
        print(key, ":", value)


# Main
if __name__ == "__main__":
    # Define the dictionary
    translator = {}
    # Loop program till exit
    while True:
    # Print out menu
        print("""
Welcome to stonks!
1. Add a stonk
2. change a price of a stonk
3. Delete a stonk
4. Print all stonks
5. Exit Program""")

        choice = input("Enter option: ")

        if choice == "1":
            translator = add(translator)
        elif choice == "2":
            translator, = edit(translator)
        elif choice == "3":
            translator = delete(translator)
        elif choice == "4":
            print_all(translator)
        elif choice == "5":
            break
        else:
            print("This option does not exist")

        for stonk in translator:
            print(stonk, percent_change)

    print("goodbye")
