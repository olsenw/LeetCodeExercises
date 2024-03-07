# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import DefaultDict, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Each number from 1 to n is grouped according to the sum of its digits.

    Return the number of groups that have the largest size.
    '''
    def countLargestGroup(self, n: int) -> int:
        d = DefaultDict(list)
        for i in range(1,n+1):
            a = sum(int(j) for j in str(i))
            d[a].append(i)
        length = 0
        count = 0
        for i in d:
            j = len(d[i])
            if length < j:
                count = 0
                length = j
            if length == j:
                count += 1
        return count

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13
        o = 4
        self.assertEqual(s.countLargestGroup(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.countLargestGroup(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)