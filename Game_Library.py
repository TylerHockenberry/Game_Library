#!/usr/bin/python3
#Tyler Hockenberry
#01/27/2020

''' This program is a library to browse through all the users owned video
games '''

#imports

#globals

#Start screen displaying options for user's selection.
def start_screen():
    print("""
    Hello! Welcome to your game library!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1) Add/Edit a game
    2) Print all games
    3) Search by title
    4) Remove a game
    5) Save Database
    
    Q) Quit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

#Adds or edits any game and it's info that's chosen by the user.
def add_edit_game():
    print()
    print("Option Add/Edit game selected!")

#Displays all games found within the library.
def print_all_games():
    print()
    print("Option Print all games selected!")

#Finds game and information based off of title given by user.
def search_by_title():
    print()
    print("Option Search by title selected!")

#Removes a selected game within database.
def remove_a_game():
    print()
    print("Option Remove a game selected!")

#Saves the Game Library.
def save_database():
    print()
    print("Option Save database selected!")

#Saves everything and exits out of the program.    
def quit():
    print()
    print("Have a great day! See ya!")

#Main
if __name__ == "__main__" :
    
    running = True
    while running:
        
        start_screen()
        users_choice = input("Please input number from desired option: ")
        
        if users_choice == "1" :
            add_edit_game()
            
        elif users_choice == "2" :
            print_all_games()
            
        elif users_choice == "3" :
            search_by_title()
            
        elif users_choice == "4" :
            remove_a_game()
            
        elif users_choice == "5" :
            save_database()
            
        elif users_choice == "Q":
            quit()
            running = False
            
        elif users_choice == "q":
            quit()
            running = False                   