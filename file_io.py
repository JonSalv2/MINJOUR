# File operations for the journaling app

import json
import os
from pathlib import Path

# Directory for the .json files.
# Uses ~/Documents/MINJOUR so journals are visible to the user, backed up by
# Time Machine/iCloud Drive, and survive re-installs of the app.
ENTRIES_DIR = Path.home() / "Documents" / "MINJOUR"


def list_files():
    """Displays all JSON files in entries directory and returns a mapping of stem -> Path."""
    files = {}

    for path in ENTRIES_DIR.glob("*.json"):
        print(path.stem)  # Shows the name without directory/extension
        files[path.stem] = path

    return files


def name_file():
    """ Prompts the user for a file name to store entries
        :return: file_name
    """
    
    default = "entries.json"
    user = input("\nEnter a file name to store your entries\n").strip()
    
    # If the user does not provide a file name, use the default
    if not user:
        return ENTRIES_DIR / default
    
    file_name = ENTRIES_DIR / f"{user}.json"

    return file_name


def write_to_file(file_name, new_data):
    """ Writes the journal entry to a JSON file
        :param file_name: path to the file
        :param new_data: new entry data
    """
    # Ensures the directory exists
    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)

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
