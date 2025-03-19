# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums.

    The following operation can be performed on on the array any number of times
    (possible zero):
    * Choose any 3 consecutive elements from the array and flip all of them.

    Flipping an element means changing its value from 0 to 1, and from 1 to 0.

    Return the minimum number of operations required to make all elements in
    nums equal to 1. If it is impossible, return -1.
    '''
    # hints give away solution
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                answer += 1
                for j in range(i, i + 3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
        return answer if sum(nums[-3:]) == 3 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,1,1,0,0]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,1,1]
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [0,0,0]
        o = 1
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)