# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n where all the integers of nums are
    in the range [1, n] and each integer appears once or twice, return an array
    of all the integers that appears twice.

    Write an algorithm that runs in O(n) time and uses only constant extra
    space.
    '''
    def findDuplicates_fails(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            x,y = nums[i], nums[nums[i] - 1]
            if x != y:
                nums[i], nums[x - 1] = y, x
        for i in range(n-1, -1, -1):
            x,y = nums[i], nums[nums[i] - 1]
            if x != y:
                nums[i], nums[x - 1] = y, x
        answer = []
        for i in range(n):
            if nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    answer.append(nums[i])
        return answer

    # uses more than constant extra space
    def findDuplicates_counter(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i in c if c[i] > 1]

    # solution based on answer by pg902421
    # https://leetcode.com/problems/find-all-duplicates-in-an-array/solutions/2523338/constant-space-solution/
    # use of modulo to derive original value of an index while using array as counter
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # remap values [1,n] -> [0,n-1] to allow easy indexes
        for i in range(n):
            nums[i] -= 1
        # add counter to the array
        for i in range(n):
            # derive the original value at index i
            j = nums[i] % n
            # imbed counter information by adding length
            nums[j] += n
        answer = []
        # find counts equal to two (have had length added twice)
        # also undoes the index remap
        return [i + 1 for i in range(n) if nums[i] >= 2 * n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,2,7,8,2,3,1]
        o = [2,3]
        self.assertEqual(s.findDuplicates(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2]
        o = [1]
        self.assertEqual(s.findDuplicates(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = []
        self.assertEqual(s.findDuplicates(i), o)

    def test_four(self):
        s = Solution()
        i = [39,31,8,14,14,38,5,15,29,49,18,6,30,47,8,35,2,17,6,10,29,46,41,48,1,36,5,28,46,39,7,47,18,42,17,11,36,45,21,33,24,10,24,50,25,16,9,12,11,25]
        o = [14,8,6,29,5,46,39,47,18,17,36,10,24,11,25]
        self.assertEqual(s.findDuplicates(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)