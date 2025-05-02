# MINJOUR.
# A minimalistic journaling app for terminal

import json
import datetime
import os

FILE_NAME = "entries.json"


def write_to_file(filename, new_data):

    # checks to see if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_entries = json.load(file)
    else:
        existing_entries = []

    # adds new data to the list
    existing_entries.extend(new_data)

    # write to file
    with open(filename, mode='w') as file:
        json.dump(existing_entries, file, indent=4)


def add_entry():

    time_stamp = datetime.datetime.now().strftime("%Y/%m/ %d %H:%M")

    entry = input()

    entry_data = [{
        "time_stamp": time_stamp,
        "entry": entry,
    }]

    return entry_data


def main():

    global FILE_NAME

    print("\n~*| MINJOUR |*~\n")
    print("A simplistic journaling app to get your ideas down quickly, in 500 characters.")
    user_input= input("press enter to continue\n")

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


if __name__ == '__main__':
    main()