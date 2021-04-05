"""
Generate folders program; create folders with corresponding amount of folders inside:
e.g. If a user selects "January", folders 1-31 will be generated inside the "January folder"
"""
MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12
MAXIMUM_YEARS = 5
NUMBER_MONTH_DICT = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                     9: "September", 10: "October", 11: "November", 12: "December"}
NUMBER_MODE_DICT = {1: "Single Mode", 2: "Range Mode", 3: "Yearly Mode"}


def main():
    display_menu()
    is_quit = False
    while not is_quit:
        try:
            menu_choice = get_valid_integer("> ")
        except ValueError:
            print("Value Error; enter a valid integer!")


def display_menu():
    print("""Welcome to the folder generator!
    Please choose from the following options:
    1. Print Instructions.
    2. Select mode.
    3. Begin program.""")


def display_instructions():
    print(f"""Instructions for the generate folders program:
    > Select mode:
    Choose from 3 different options when changing generation modes:
    ~Single month mode:
    \tEnter a month number between {MINIMUM_MONTH}-{MAXIMUM_MONTH} and generate its folder and the corresponding\
    amount of folders; e.g. enter 1 and a January folder will generate with 31 folders labeled 1-31.
    ~Range mode:
    \tEnter a range between {MINIMUM_MONTH} - {MAXIMUM_MONTH} and generate all those months' folders and corresponding\
    amount of folders; e.g. 1-3 will generate January-March and their corresponding amount of folders
    ~Year mode:
    \tEnter the amount of years you wish to generate (max. {MAXIMUM_YEARS}) and generate all those years folders,\
    corresponding months, and the months' corresponding folders.
    ~Exit:
    \tQuit.""")


def get_valid_integer(prompt):
    is_valid_integer = False
    while not is_valid_integer:
        try:
            valid_integer = int(input(prompt))
            if MINIMUM_MONTH < valid_integer > MAXIMUM_MONTH:
                print(f"Boundary error; enter a valid integer between {MINIMUM_MONTH} - {MAXIMUM_MONTH}")
            else:
                return valid_integer
        except ValueError:
            print(f"Value Error, enter a valid integer between {MINIMUM_MONTH} and {MAXIMUM_MONTH}!")
        is_valid_integer = True
