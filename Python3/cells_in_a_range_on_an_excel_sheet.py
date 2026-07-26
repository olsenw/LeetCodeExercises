# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A cell (r, c) of an excel sheet is represented as a string "<col><row>"
    where:
    * <col> denotes the column number c of the cell. It is represented by
      alphabetical letters.
    * <row> is the row number r of the cell. The rth row is represented by the
      integer r.
    
    Given a string s in the format "<col1><row1>:<col2><row2>", where <col1> 
    represents the column c1, <row1> represents the row r1, <col2> represents
    the column c2, and <row2> represents the row r2, such that r1 <= r2 and
    c1 <= c2.

    Return the list of cells (x,y) such that r1 <= x <= r2 and c1 <= y <= c2.
    The cells should be represented as strings in the format mentioned above and
    be sorted in non-decreasing order first by columns and then by rows.
    '''
    def cellsInRange(self, s: str) -> List[str]:
        answer = []
        c1,r1,c2,r2 = ord(s[0]),ord(s[1]),ord(s[3]),ord(s[4])
        for c in range(c1, c2+1):
            for r in range(r1,r2+1):
                answer.append(f'{chr(c)}{chr(r)}')
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "K1:L2"
        o = ["K1","K2","L1","L2"]
        self.assertEqual(s.cellsInRange(i), o)

    def test_two(self):
        s = Solution()
        i = "A1:F1"
        o = ["A1","B1","C1","D1","E1","F1"]
        self.assertEqual(s.cellsInRange(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)