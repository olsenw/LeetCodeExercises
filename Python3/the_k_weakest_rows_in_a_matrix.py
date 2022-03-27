# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an mxn binary matrix mat of 1's (representing soldiers) and 
    0's (representing civilians). The soldiers are positioned in front
    of the civilians. Thats is all the 1's will appear to the left of
    all the 0's in in each row.

    A row i is weaker than a row j if one of the following is true:
    * The number of soldiers in row i is less than the number of
      soldiers in row j.
    * Both rows have the same number of soldiers and i < j.

    Return the indices of the k weakest rows in the matrix ordered from
    weakest to strongest.
    '''
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _,i in sorted((sum(r),i) for i,r in enumerate(mat))[:k]]

    '''
    There are a bunch of ways to solved this problem, like using a min
    heap and an index that advances until a zero is found.

    These other solutions just may not see benefit in python except in
    some extreme corner cases.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]]
        j = 3
        o = [2,0,3]
        self.assertEqual(s.kWeakestRows(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]]
        j = 2
        o = [0,2]
        self.assertEqual(s.kWeakestRows(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)