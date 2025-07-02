#!/usr/bin/python3
"""XML serialization and deserialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): XML filename to read from.

    Returns:
        dict: Deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
