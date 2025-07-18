# MINJOUR.
# A minimalistic journaling app for terminal

import actions
import file_io
import json
import os


def main():
    """ Main function to run the journaling app """

    print("\n~~~~*| MINJOUR |*~~~~\n")
    print("A simplistic journaling app to get your thoughts down quickly, in 500 characters.\n")
    
    # Allows the user to name the file where entries will be stored, defaults to "entries.json"
    file_name = file_io.name_file()

    while True:

        # Prompts the user for input to add a new entry, read existing entries, delete an entry, or quit
        user_input= input("\npress (enter) for a new entry\npress (r) to read your entries\npress (d) to delete an entry\npress (q) to quit\n")

        try:

            # Checking for "Enter" as input
            if user_input.strip() == "": 

                

                while True:

                    print("~~~~~~((((Whats on your mind?))))~~~~~~\n")

                    # Prompts the user to enter a new journal entry
                    new_entry = actions.add_entry(file_name)
                    
                    # If the entry is not empty, write it to the file
                    if new_entry is not None:
                        file_io.write_to_file(file_name, new_entry)

                    # Checks if the user wants to make another entry
                    user_input = input("\nMake another entry (press y or n)? \n")
                    if user_input == "y":
                        continue
                    else:
                        break
                
            # If the user wants to read existing entries            
            elif user_input == "r":

                print("\n~~~~~~((((Your entries))))~~~~~~\n")
                actions.show_entries(file_name)
                continue
            
            # If the user wants to delete an entry
            elif user_input == "d":

                print("~~~~~~((((Delete an entry))))~~~~~~\n")
                print("Select an entry to delete by inputing the number of its corresponding ID\n")
                actions.delete_entry(file_name)
                continue
            
            # If the user wants to quit the app
            elif user_input == "q":

                print("~~~~~~((((Goodbye))))~~~~~~\n")
                return
            
            else:
                print("\nInvalid input. Please try again.\n")

        except TypeError as terr:
            print(f"\nType Error: {terr}")
        except FileNotFoundError:
            print("\nEntries file not found. Please add an entry first.")
        except json.JSONDecodeError:
            print("\nEntries file is corrupted or not valid JSON.")


if __name__ == '__main__':
    main()
