#!/usr/bin/python3
"""Basic serialization module."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Data to serialize.
        filename (str): Output JSON filename.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): Input JSON filename.

    Returns:
        dict: Deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
