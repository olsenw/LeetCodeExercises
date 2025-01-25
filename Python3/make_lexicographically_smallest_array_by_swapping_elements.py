# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of positive integers nums and a positive integer
    limit.

    In one operation, choose any two indices i and j and swap nums[i] and
    nums[j] if abs(nums[i] - nums[j]) <= limit.

    Return the lexicographically smallest array that can be obtained by
    performing the operation any number of times.

    An array a is lexicographically smaller than an array b if in the first
    position where a and b differ, array a has an element that is less than the
    corresponding element in b.
    '''
    # based on leet code solution
    # lot of back and forth tracking of groups to lists
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        numSort = sorted(nums)

        group = 0
        numGroup = {numSort[0]: group}
        groupList = {group: [numSort[0]]}

        for i in range(1, len(nums)):
            if abs(numSort[i] - numSort[i-1]) > limit:
                # new group
                group += 1
            numGroup[numSort[i]] = group
            if group not in groupList:
                groupList[group] = []
            groupList[group].append(numSort[i])

        for i in range(len(nums)):
            group = numGroup[nums[i]]
            nums[i] = groupList[group].pop(0)
        
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,3,9,8], 2
        o = [1,3,5,8,9]
        self.assertEqual(s.lexicographicallySmallestArray(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,7,6,18,2,1], 3
        o = [1,6,7,18,1,2]
        self.assertEqual(s.lexicographicallySmallestArray(*i), o)

    def test_three(self):
        s = Solution()
        i = [1,7,28,19,10], 3
        o = [1,7,28,19,10]
        self.assertEqual(s.lexicographicallySmallestArray(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)