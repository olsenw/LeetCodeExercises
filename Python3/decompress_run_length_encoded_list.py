# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list nums of integers representing a list compressed with run-length
    encoding.

    Consider each adjacent pair of elements
    [freq, val] = [nums[2*j], nums[2*i+1]] (with i >= 0). For each such pair,
    there are freq elements with value val concentrated in a sublist.
    Concentrate all the sublists from left to right to generate the decompressed
    list.

    Return the decompressed list.
    '''
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums) // 2):
            freq = nums[2*i]
            val = nums[2*i + 1]
            for _ in range(freq):
                answer.append(val)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = [2,4,4,4]
        self.assertEqual(s.decompressRLElist(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,3]
        o = [1,3,3]
        self.assertEqual(s.decompressRLElist(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)