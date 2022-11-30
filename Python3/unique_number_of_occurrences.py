# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers arr, return true if the number of occurrences of
    each value in the array is unique, or false otherwise.
    '''
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for v in c.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,1,1,3]
        o = True
        self.assertEqual(s.uniqueOccurrences(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = False
        self.assertEqual(s.uniqueOccurrences(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)