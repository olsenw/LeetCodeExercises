# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array data representing the data, return whether it
    is a valid UTF-8 encoding (ie it translates to a sequence of valid
    UTF-8 encoded characters).

    A character in UTF8 can be from 1 to 4 bytes long, subjected to the
    following rules:
    1) For a 1-byte character, the first bit is a 0, followed by its
       Unicode code.
    2) For an n-bytes character, the first n bits are all one's, the
       n + 1 bytes with the most significant 2 bits being 10.
    
    Explanation of how this works, along with a diagram exists on
    Leetcode problem description.

    Note: The input is an array of integers. Only the least significant
    8 bits of each integer is used to store the data. This means each
    integer represents only 1 byte of data.
    '''
    # passes but slow
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            if data[i] < 0b1000_0000:
                i += 1
            elif data[i] & 0b1110_0000 == 0b1100_0000 and i+1 < len(data):
                if data[i+1] & 0b1100_0000 != 0b1000_0000:
                    return False
                i += 2
            elif data[i] & 0b1111_0000 == 0b1110_0000 and i+2 < len(data):
                if data[i+1] & 0b1100_0000 != 0b1000_0000:
                    return False
                if data[i+2] & 0b1100_0000 != 0b1000_0000:
                    return False
                i += 3
            elif data[i] & 0b1111_1000 == 0b1111_0000 and i+3 < len(data):
                if data[i+1] & 0b1100_0000 != 0b1000_0000:
                    return False
                if data[i+2] & 0b1100_0000 != 0b1000_0000:
                    return False
                if data[i+3] & 0b1100_0000 != 0b1000_0000:
                    return False
                i += 4
            else:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [197,130,1]
        o = True
        self.assertEqual(s.validUtf8(i), o)

    def test_two(self):
        s = Solution()
        i = [235,140,4]
        o = False
        self.assertEqual(s.validUtf8(i), o)

    def test_three(self):
        s = Solution()
        i = [240,162,138,147]
        o = True
        self.assertEqual(s.validUtf8(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)