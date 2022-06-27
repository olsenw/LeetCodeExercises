# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A decimal number is called deci-binary if each of its digits is
    either 0 to 1 without any leading zeros. For example, 101 and 1100
    are deci-binary, while 112 and 3001 are not.

    Given a string n that represents a positive decimal integer, return
    the minimum number of positive deci-binary numbers needed so that
    they sum up to n.
    '''
    def minPartitions(self, n: str) -> int:
        return ord(max(n)) - ord('0')

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "32"
        o = 3
        self.assertEqual(s.minPartitions(i), o)

    def test_two(self):
        s = Solution()
        i = "82734"
        o = 8
        self.assertEqual(s.minPartitions(i), o)

    def test_three(self):
        s = Solution()
        i = "27346209830709182346"
        o = 9
        self.assertEqual(s.minPartitions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)