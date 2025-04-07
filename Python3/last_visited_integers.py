# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums where nums[i] is either a positive integer or
    -1. For each -1 find the respective positive integer, which is called the
    last visited integer.

    To achieve this goal, define two empty arrays: seen and ans.

    Start iterating from the beginning of the array nums.
    * If a positive integer is encountered, prepend it to the front of seen.
    * If -1 is encountered, let k be the number of consecutive -1's seen so far
      (including the current -1).
      * If k is less than or equal to the length of seen, append the k-th
        element of seen to ans.
      * If k is strictly greater than the length of seen, append -1 to ans.
    
    Return the array ans.
    '''
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        answer = []
        seen = deque()
        k = 0
        for n in nums:
            if n > 0:
                seen.appendleft(n)
                k = 0
            else:
                k += 1
                if k > len(seen):
                    answer.append(-1)
                else:
                    answer.append(seen[k-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,-1,-1,-1]
        o = [2,1,-1]
        self.assertEqual(s.lastVisitedIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = [1,-1,2,-1,-1]
        o = [1,2,1]
        self.assertEqual(s.lastVisitedIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)