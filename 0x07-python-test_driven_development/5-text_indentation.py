#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a new text string with proper indentation
    new_text = ""
    for char in text:
        new_text += char
        if char in ('.', '?', ':'):
            new_text += "\n\n"

    # Print the formatted text
    print(new_text, end="")
