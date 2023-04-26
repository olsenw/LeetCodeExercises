# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
    Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above.

    Neat graphic depicting Pascal's triangle.
    '''
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1,1]
        for i in range(1, rowIndex):
            update = [1] * (len(row) + 1)
            for j in range(1, i+1):
                update[j] = row[j-1] + row[j]
            row = update
        return row

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = [1,3,3,1]
        self.assertEqual(s.getRow(i), o)

    def test_two(self):
        s = Solution()
        i = 0
        o = [1]
        self.assertEqual(s.getRow(i), o)

    def test_three(self):
        s = Solution()
        i = 1
        o = [1,1]
        self.assertEqual(s.getRow(i), o)

    def test_four(self):
        s = Solution()
        i = 2
        o = [1,2,1]
        self.assertEqual(s.getRow(i), o)

    def test_five(self):
        s = Solution()
        i = 4
        o = [1,4,6,4,1]
        self.assertEqual(s.getRow(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)