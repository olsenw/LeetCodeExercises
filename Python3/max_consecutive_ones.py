# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums, return the maximum number of consecutive 1's in
    the array.
    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        for n in nums:
            if n:
                count += 1
                answer = max(answer, count)
            else:
                count = 0
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,0,1,1,1]
        o = 3
        self.assertEqual(s.findMaxConsecutiveOnes(i), o)

    def test_two(self):
        s = Solution()
        i = [1,0,1,1,0,1]
        o = 2
        self.assertEqual(s.findMaxConsecutiveOnes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)