def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj (object): Instance of a class.

    Returns:
        dict: Dictionary of all attributes of obj.
    """
    return obj.__dict__.copy()
