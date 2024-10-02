# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, replace each element with its rank.
    
    The rank represents how large the element is. The rank has the following
    rules:
    * Rank is an integer starting from 1.
    * The larger the element, the larger the rank. If two elements are equal,
      their rank must be the same.
    * Rank should be as small as possible.
    '''
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {j:i for i,j in enumerate(sorted(set(arr)), 1)}
        return [d[i] for i in arr]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [40,10,20,30]
        o = [4,1,2,3]
        self.assertEqual(s.arrayRankTransform(i), o)

    def test_two(self):
        s = Solution()
        i = [100,100,100]
        o = [1,1,1]
        self.assertEqual(s.arrayRankTransform(i), o)

    def test_three(self):
        s = Solution()
        i = [37,12,28,9,100,56,80,5,12]
        o = [5,3,4,2,8,6,7,1,3]
        self.assertEqual(s.arrayRankTransform(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)