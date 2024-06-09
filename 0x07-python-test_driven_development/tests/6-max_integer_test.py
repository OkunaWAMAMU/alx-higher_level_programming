#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test when list is not empty
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        
        # Test when list is empty
        self.assertIsNone(max_integer([]))
        
        # Test when list contains negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
        # Test when list contains a single element
        self.assertEqual(max_integer([5]), 5)
        
        # Test when list contains duplicate elements
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        
        # Test when list contains floating point numbers
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        
        # Test when list contains mixed integers and floats
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        
        # Test when list contains large numbers
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)
        
        # Test when list contains zero
        self.assertEqual(max_integer([0]), 0)

if __name__ == "__main__":
    unittest.main()
