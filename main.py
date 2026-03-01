# MINJOUR.
# A minimalistic journaling app for terminal

import actions
import file_io
import json


def main():
    """ Main function to run the app """

    print("\n      ~~~~~~~~~~*****| MINJOUR |*****~~~~~~~~~~           \n")
    print("A simple journaling app to get your thoughts down quickly.\n\n")
    
    while True:
        
        print("Would you like to create a new file or open an existing one?\n")
        user_select = input("Press (n) to create a new file\nPress (o) to open an existing file\nPress (q) to quit\n")

        if user_select.strip() == "n":
            # Allows the user to name the file where entries will be stored, defaults to "entries.json"
            file_name = file_io.name_file()

        elif user_select.strip() == "o":
            # Lists existing files in the current directory and prompts the user to select one
            print("")
            file_map = file_io.list_files()
            file_select = input("\nEnter the name of the file you want to open\n").strip()

            if file_select not in file_map:
                print(f"\n{file_select} does not exist in the entries directory. Please create a new file or choose an existing one.\n")
                continue
            else:
                # Sets the file name to the selected file
                print(f"\nYou have selected {file_select}.")
                file_name = file_map[file_select]          

        elif user_select.strip() == "q":
            print("\n~~~~~~((((Goodbye!))))~~~~~~\n")
            return

        else:
            print("\nInvalid input. Please try again.\n")
            continue

        while True:

            try:
                # Prompts the user for input to add a new entry, read existing entries, delete an entry, or quit
                user_input = input("\npress (enter) for a new entry,\npress (r) to read your entries\npress (d) to delete an entry\npress (m) to return to main menu\npress (q) to quit\n")

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
                        if user_input.strip() == "y":
                            continue
                        else:
                            break
                    
                # If the user wants to read existing entries            
                elif user_input.strip() == "r":

                    print("\n~~~~~~((((Your entries))))~~~~~~\n")
                    actions.show_entries(file_name)
                    continue
                
                # If the user wants to delete an entry
                elif user_input.strip() == "d":

                    print("~~~~~~((((Delete an entry))))~~~~~~\n")
                    print("Select an entry to delete by inputing the number of its corresponding ID\n")
                    actions.delete_entry(file_name)
                    continue
                
                # If the user wants to return to the main menu
                elif user_input.strip() == "m":

                    print("\n~~~~~~((((Returning to main menu))))~~~~~~\n")
                    break

                # If the user wants to quit the app
                elif user_input.strip() == "q":

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
