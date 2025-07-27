# Actions that allow users to add, read, and delete journal entries.

import json
import datetime 
import os
import re

def add_entry(file_name):
    """ Prompts the user to enter a new journal entry
        :return: entry_data: a list of key/values pairs containing new movie data
    """
    
    # Get the current date and time (YYYY/MM/DD HH:MM)
    time_stamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

    # Prompt the user for a new entry
    entry = input()

    # Sets the entry ID to 1 if no file exists and increments it for each new entry
    if os.path.exists(file_name):
        # checkes to see if the file exits 
        with open(file_name, "r") as file:
            existing_entries = json.load(file)          
            current_id = len(existing_entries) + 1
    else:
        current_id = 1

    # Validates the entry 
    if entry == "":
        print("~(Your entry is empty and was not saved)~")
        return 
    else:
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
                print("\n")
    else:
        raise FileNotFoundError("No entries found. Please add an entry first.")


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
        raise FileNotFoundError("No entries found.")

    # Prompts the user to select the entry they want to delete
    entry_to_delete = input()
    if re.search(r"^\d+$", entry_to_delete) is None:
        raise TypeError("Please enter an integer from 1 to 9999")

    # Checks if the entry exists and deletes it
    for entry in existing_entries:
        if int(entry['id']) == int(entry_to_delete):
            existing_entries.remove(entry)
            print(f"Entry {entry_to_delete} deleted.")

            # Reassign entry IDs to ensure they match the current order
            for index, entry in enumerate(existing_entries, start=1):
                entry['id'] = index

            # Writes the updated entries back to the file
            with open(file_name, mode='w') as file:
                json.dump(existing_entries, file, indent=4)
            break
    else:   
        print(f"Entry {entry_to_delete} not found.")