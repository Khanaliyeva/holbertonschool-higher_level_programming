#!/usr/bin/python3
"""Convert CSV file to JSON file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file data to JSON and save to data.json.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open('data.json', mode='w') as jsonfile:
            json.dump(data, jsonfile)

        return True
    except Exception:
        return False
