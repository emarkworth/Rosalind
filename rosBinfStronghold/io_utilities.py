#!user/bin/env python3
"""
filename: io_utilities.py

Contains the functions gc_content, file_handler for use in Rosalind coding questions.
"""


def gc_content(string):
    """Function takes a string and returns the percent of Gs and Cs within.
    @param string: The sequence to be analyzed
    @:return: The GC content of the sequence"""
    # Establish numerator and denominator
    gc_amount = 0

    # Count Gs and Cs
    for char in string:
        if char in ['G', 'C']:
            gc_amount += 1

    # Raise exception for divide by zero
    try:
        gc_percent = gc_amount / len(string)
        return gc_percent
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")

def file_handler(file=None, mode=None):
    """
    Takes : 2 arguments file name and mode i.e. what is needed to be done with
    this file. This function opens the file based on the mode passed in
    the argument and returns filehandle.
    @param file: The file to open for the mode
    @param mode: They way to open the file, e.g. reading, writing, etc
    @return: filehandle
    """

    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {file} in mode '{mode}'")
        raise
    except ValueError:
        print(f"Could not open the file: {file} in mode '{mode}'")
        raise
