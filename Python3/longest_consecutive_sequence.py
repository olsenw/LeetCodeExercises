# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an unsorted array of integers nums, return the length of the
    longest consecutive elements sequence.

    Write an algorithm that runs in O(n) time.
    '''
    # sorts the elements and then iterates through them to find sequence
    # O(n log n) time
    def longestConsecutive_sort(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        c = m = 1
        p = nums[0]
        for n in nums[1:]:
            if p == n:
                continue
            elif p + 1 == n:
                c += 1
            else:
                m = max(m, c)
                c = 1
            p = n
        return max(m, c)
    
    def longestConsecutive_sort_faster(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        c = m = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            elif nums[i-1] + 1 == nums[i]:
                c += 1
            else:
                m = max(m, c)
                c = 1
        return max(m, c)

    # Based on leetcode solution (not faster than sorting
    # [python's sort is well optimized...])
    # O(n) time O(n) space
    # Basically check if an element is the lowest possible for its
    # sequence (ie first element in sequence) and find length of that
    # sequence.
    # This is an improvement on the O(n^3) brute force solution by using
    # a set for lookups and only evaluating sequences if current element
    # is the first element in the sequence.
    def longestConsecutive(self, nums: List[int]) -> int:
        # allow constant time lookups
        s = set(nums)
        # needs to be zero for len(nums) == 0
        m = 0
        # check each element as start of a sequence
        for n in nums:
            # force starts on lowest element in sequence
            # ie element is lowest possible in sequence
            if n - 1 not in s:
                p = n
                c = 1
                # find sequence length
                while p + 1 in s:
                    p += 1
                    c += 1
                m = max(m, c)
        return m


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [100,4,200,1,3,2]
        o = 4
        self.assertEqual(s.longestConsecutive(i), o)

    def test_two(self):
        s = Solution()
        i = [0,3,7,2,5,8,4,6,0,1]
        o = 9
        self.assertEqual(s.longestConsecutive(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,2,2,3]
        o = 3
        self.assertEqual(s.longestConsecutive(i), o)

    def test_four(self):
        s = Solution()
        i = []
        o = 0
        self.assertEqual(s.longestConsecutive(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)