#!/usr/bin/python3


class MyList(list):
    """A class that inherits from list and provides a print_sorted method."""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
