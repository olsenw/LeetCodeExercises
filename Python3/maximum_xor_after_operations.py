# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. In one operation, select any
    non-negative integer x and an index i, then update nums[i] to be equal to
    nums[i] AND (nums[i] XOR x).

    Note that AND is the bitwise AND operation and XOR is the bitwise XOR
    operation.

    Return the maximum possible bitwise XOR of all elements of nums after
    applying the operation any number of times.
    '''
    def maximumXOR_fails(self, nums: List[int]) -> int:
        m = max(nums)
        i = 1
        while i < m:
            i <<= 1
        return i-1

    # trick is the operation can be made into bitwise OR
    def maximumXOR(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            answer |= n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,4,6]
        o = 7
        self.assertEqual(s.maximumXOR(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,9,2]
        o = 11
        self.assertEqual(s.maximumXOR(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)