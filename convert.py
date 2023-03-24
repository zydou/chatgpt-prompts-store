#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv  # Import module 'csv' for reading/writing to CSV files
import json  # Import module 'json' for working with JSON files
import os  # Import module 'os' for accessing operating system functionalities

# Join file/directory paths with respect to the current platform ("/" for UNIX, "\" for Win)
CSV_FILE = os.path.join("upstream", "prompts.csv")

# Asserts if CSV_FILE exists as a normal file i.e, if it is not a directory, symbolic link,etc.
# AssertionError arises if CSV_FILE does not exist
assert os.path.isfile(CSV_FILE)

json_data = []  # Create an empty list for all dictionary objects to store later

# Open the CSV file and loop through each row, assert there are only 2 columns per row,
# Add key-value pairs of 1st and 2nd column values as 'act' and 'prompt', respectively in a new dictionary object.
# Then append that dictionary object to the json_data list previously created
with open(CSV_FILE, newline="") as csvfile:  # Use 'with' statement (a context manager) to work with files cleanly
    rows = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in rows:
        assert len(row) == 2  # Assert that each row has only 2 columns
        act, prompt = row  # Assign first and second column values into variables act and prompt
        json_data.append(
            {
                "act": act,
                "prompt": prompt.replace('"', "'"),  # convert double quotes to single quotes
            }
        )  # Add a new dictionary object to the list

# Write the json data containing dictionaries with 'act' and 'prompt' keys to prompts.json file.
# Ensure that edges aren´t cut, is indented for clarity of understanding and easy reading.
with open("prompts.json", "w") as file_handle:
    json.dump(json_data[1:], file_handle, indent=2)
