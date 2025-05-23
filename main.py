# MINJOUR.
# A minimalistic journaling app for terminal

import json
import datetime
import os

FILE_NAME = "entries.json"


def write_to_file(file_name, new_data):
    """ Writes the movie data to a JSON file
        :param file_name: path to the file
        :param new_data: new entry data
    """

    # checks to see if the file exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            existing_entries = json.load(file)
    else:
        existing_entries = []

    # adds new data to the list
    existing_entries.extend(new_data)

    # write to file
    with open(file_name, mode='w') as file:
        json.dump(existing_entries, file, indent=4)


def add_entry():
    """ Prompts the user to enter a new journal entry
        :return: entry_data: a list of key/values pairs containing new movie data
    """
    
    # Get the current date and time (YYYY/MM/DD HH:MM)
    time_stamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

    # Prompt the user for a new entry
    entry = input()

    # checkes to see if the file exits 
    # Sets the entry ID to 1 if no file exists and increments it for each new entry
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            existing_entries = json.load(file)          
            current_id = len(existing_entries) + 1
    else:
        current_id = 1

    # Stores the entry data in a dictionary and adds timestamp and index ID
    entry_data = [{
        "id": current_id,
        "time_stamp": time_stamp,
        "entry": entry,
    }]

    return entry_data


def show_entries(file_name):
    """ Displays the entries in the entires.json file
        :param file_name: path to the file
    """

    # Checks if the file exists
    if os.path.exists(file_name):

        # Loads the existing entries from the file
        with open(file_name, "r") as file:
            existing_entries = json.load(file)

            # Prints the entries
            for entry in existing_entries:
                print(f"{entry['time_stamp']}: {entry['entry']}")


def delete_entry(file_name):
    """ Deletes an entry in the entires.json file
        :param file_name: path to the file
    """

    # Checks if the file exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            existing_entries = json.load(file)
            # Prints the entries
            for entry in existing_entries:
                print(f"{entry['id']}: {entry['time_stamp']}: {entry['entry']}")
    else:
        print("No entries to delete.")

    # Prompts the user to select the entry they want to delete
    entry_to_delete = int(input())

    # Checks if the entry exists and deletes it
    for entry in existing_entries:
        if int(entry['id']) == entry_to_delete:
            existing_entries.remove(entry)
            print(f"Entry {entry_to_delete} deleted.")

            # Writes the updated entries back to the file
            with open(file_name, mode='w') as file:
                json.dump(existing_entries, file, indent=4)
            break
    else:   
        print(f"Entry {entry_to_delete} not found.")


def main():

    global FILE_NAME

    print("\n~*| MINJOUR |*~\n")
    print("A simplistic journaling app to get your ideas down quickly, in 500 characters.")
    
    user_input= input("press (enter) for a new entry\npress (r) to read your entries\npress (d) to delete an entry\npress (q) to quit\n")

    if user_input == "":
        while True:

            print("~~~~~~((((Whats on your mind?))))~~~~~~\n")

            new_data = add_entry()
            write_to_file(FILE_NAME, new_data)

            user_input = input("Make another entry (press y or n)? \n")

            if user_input == "y":
                continue
            else:
                return

    elif user_input == "r":
        print("~~~~~~((((Your entries))))~~~~~~\n")
        show_entries(FILE_NAME)
        return
    
    elif user_input == "d":
        print("~~~~~~((((Delete an entry))))~~~~~~\n")
        print("Select an entry to delete by inputing the number of its corresponding ID\n")
        delete_entry(FILE_NAME)
        return

    elif user_input == "q":
        print("Goodbye!")
        return

if __name__ == '__main__':
    main()