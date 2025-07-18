# File operations for the journaling app

import json
import os


def name_file():
    """ Prompts the user for a file name to store entries
        :return: file_name
    """
    
    default = "entries.json"
    user_name = input("Enter a file name to store your entries\n").strip()
    
    # If the user does not provide a file name, use the default
    if not user_name.strip():
        return default.strip()
    
    file_name = f"{user_name.strip()}.json"

    return file_name


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