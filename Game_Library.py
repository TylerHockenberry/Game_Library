#!/usr/bin/python3
#Tyler Hockenberry
#01/27/2020

''' This program is a library to browse through all the users owned video
games '''

#imports

#globals
def start_screen():
    print("Hello! Welcome to your game library!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("1) Add/Edit game")
    print("2) Print all games")
    print("3) Search by title")
    print("4) Remove a game")
    print("5) Save Database")
    print()
    print("Q) Quit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def add_edit_game():
    print()
    print("Option Add/Edit game selected!")

def print_all_games():
    print()
    print("Option Print all games selected!")
    
def search_by_title():
    print()
    print("Option Search by title selected!")

def remove_a_game():
    print()
    print("Option Remove a game selected!")

def save_database():
    print()
    print("Option Save database selected!")
    
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