#!/usr/bin/python3
#Tyler Hockenberry
#01/27/2020

''' This program is a library to browse through all the users owned video
games '''

#imports
#Added Jan 28, 2020 v
import pickle
#Added Jan 28, 2020 ^

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
    print("""
    Option Add/Edit game selected! """)

#Displays all games found within the library.
def print_all_games():
    #Borrowed from MR. Schmidt's big_brother.py v
    key_list = games.keys()

    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("Platform: ", games[key][4])
        print("Year Published: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single or Multiplayer: ", games[key][7])
        print("Price: ", games[key][8])
        print("Completed: ", games[key][9])
        print("Date of Purchase: ", games[key][10])
        print("----------------------")
     
        
#Finds game and information based off of title given by user.
def search_by_title():
    print("""
    Option Search by title selected! """)

#Removes a selected game within database.
def remove_a_game():
    print("""
    Option Remove a game selected! """)

#Saves the Game Library.
def save_database():
    pickle_file = open("game_lib.pickle", "wb")
    pickle.dump(games, pickle_file)
    pickle_file.close() 
    print("Save Completed!")
    

#Saves everything and exits out of the program.    
def quit():
    print("""
    Have a great day! See ya! """)

#Main
games = {}
pickle_file = open("game_lib.pickle", "rb")
games = pickle.load(pickle_file)
pickle_file.close()

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