# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    An element x of an integer array arr of length m is dominant if more than
    half the elements of arr have a value of x.

    Given a 0-indexed integer array nums of length n with one dominant element.

    It is possible to split nums at an index i into two arrays nums[0, ..., i]
    and nums[i+1, ..., n-1], but the split is only valid if:
    * 0 <= i < n - 1
    * nums[0, ..., i], and nums[i+1, ..., n-1] have the same dominant element.

    Here, nums[i, ..., j] denotes the subarray of nums starting at index i and
    ending at index j, both ends being inclusive. Particularly, if j < i then
    nums[i, ..., j] denotes an empty subarray.

    Return the minimum index of a valid split. If no valid split exists return
    -1.
    '''
    def minimumIndex(self, nums: List[int]) -> int:
        dominant, count = Counter(nums).most_common(1)[0]
        c = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                c += 1
                count -= 1
                # note, multiple count by two is easy way to see if dominate subarray
                # 2 * dominant_count > length_subarray
                if c * 2 > i + 1 and 2 * count > (len(nums) - i - 1):
                    return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,2]
        o = 2
        self.assertEqual(s.minimumIndex(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,3,1,1,1,7,1,2,1]
        o = 4
        self.assertEqual(s.minimumIndex(i), o)

    def test_three(self):
        s = Solution()
        i = [3,3,3,3,7,2,2]
        o = -1
        self.assertEqual(s.minimumIndex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)