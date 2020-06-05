import copy
import random

def duplicate_objects(objects, desired_number):
    """
    Appends duplicate objects to a list until a new desired number is achieved

    Args:
        objects: original list of objects
        desired_number: Desired number of total objects

    Returns:
        objects: List of objects with the duplicates
    """
    orig_length = len(objects)
    if orig_length >= desired_number:
        return objects

    while len(objects) < desired_number:
        dummy = copy.deepcopy(objects[random.randint(0,orig_length)])

        try:
            dummy.id = random.randint(orig_length,orig_length + desired_number)
        except:
            pass

        objects.append(dummy)
    return objects
