# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n which represents an array nums containing the numbers
    from 1 to n in order. Additionally given a 2D array conflictingPairs, where
    conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

    Remove exactly one element from conflictingPairs. Afterward, count the
    number of non-empty subarrays of nums which do not both contain a and b for
    any remaining conflicting pair [a,b].

    Return the maximum number of subarrays possible after removing exactly one
    conflicting pair.
    '''
    # based on LeetCode editorial
    # mystery why works
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        a = [float('inf')] * (n + 1)
        b = [float('inf')] * (n + 1)
        for pair in conflictingPairs:
            i,j = min(pair), max(pair)
            if a[i] > j:
                b[i] = a[i]
                a[i] = j
            elif b[i] > j:
                b[i] = j
        answer = 0
        x,y = n, float('inf')
        delCount = [0] * (n + 1)
        for i in range(n, 0, -1):
            if a[x] > a[i]:
                y = min(y, a[x])
                x = i
            else:
                y = min(y, a[i])
            answer += min(a[x], n + 1) - i
            delCount[x] += min(y, b[x], n + 1) - min(a[x], n + 1)
        return answer + max(delCount)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[2,3],[1,4]]
        o = 9
        self.assertEqual(s.maxSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[1,2],[2,5],[3,5]]
        o = 12
        self.assertEqual(s.maxSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)