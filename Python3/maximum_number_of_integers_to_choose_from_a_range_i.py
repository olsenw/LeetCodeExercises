# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array banned and two integers n and maxSum. Choose some
    number of integers following the below rules.
    * The chosen integers have to be in the range [1,n].
    * Each integer can be chosen at most once.
    * The chosen integers should not be in the array banned.
    * The sum of the chosen integers should not exceed maxSum.

    Return the maximum number of integers that can chosen following the
    mentioned rules.
    '''
    # fails because banned can have repeat numbers in it
    # knock on effect of breaking the return math (skipped same number should only count once...)
    def maxCount_fails(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        s = 0
        j = 0
        for i in range(1, n+1):
            # problem: banned repeat numbers
            if j < len(banned) and i == banned[j]:
                j += 1
            elif s + i > maxSum:
                # problem: over count banned repeat numbers
                return i - j - 1
            else:
                s += i
        return n - j

    # help from hints
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s = 0
        a = 0
        for i in range(1,n+1):
            if i in banned:
                continue
            elif s + i > maxSum:
                break
            else:
                s += i
                a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,6,5]
        j = 5
        k = 6
        o = 2
        self.assertEqual(s.maxCount(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,6,7]
        j = 8
        k = 1
        o = 0
        self.assertEqual(s.maxCount(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [11]
        j = 7
        k = 50
        o = 7
        self.assertEqual(s.maxCount(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [87,193,85,55,14,69,26,133,171,180,4,8,29,121,182,78,157,53,26,7,117,138,57,167,8,103,32,110,15,190,139,16,49,138,68,69,92,89,140,149,107,104,2,135,193,87,21,194,192,9,161,188,73,84,83,31,86,33,138,63,127,73,114,32,66,64,19,175,108,80,176,52,124,94,33,55,130,147,39,76,22,112,113,136,100,134,155,40,170,144,37,43,151,137,82,127,73]
        j = 1079
        k = 87
        o = 9
        self.assertEqual(s.maxCount(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)