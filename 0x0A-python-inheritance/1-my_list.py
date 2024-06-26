#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
