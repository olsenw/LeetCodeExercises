# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums and an integer k, return true if there are two
    distinct indices i and j in the array such that nums[i] == nums[j] and
    abs(i - j) <= k.
    '''
    # O(n k) time because k can be n this is O(n^2)
    def containsNearbyDuplicate_tle(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,min(len(nums), i+k+1)):
                if nums[i] == nums[j]:
                    return True
        return False

    # O(n) time
    def containsNearbyDuplicate_slow(self, nums: List[int], k: int) -> bool:
        h = {nums[0]:0}
        for i in range(1, len(nums)):
            if nums[i] in h:
                if abs(h[nums[i]] - i) <= k:
                    return True
                h[nums[i]] = i
            else:
                h[nums[i]] = i
        return False

    # copied as note from leetcode 640ms submission
    # https://leetcode.com/submissions/api/detail/219/python3/640/
    def containsNearbyDuplicate_fast(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r -l > k :  # the order matters here between this and the next if. If we check for nums[r] too early and don't first remove nums[l] when we need to then we return the wrong result.
                window.remove(nums[l])
                l +=1
            if nums[r] in window:
                return True
          
            window.add(nums[r])
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1]
        j = 3
        o = True
        self.assertEqual(s.containsNearbyDuplicate(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,0,1,1]
        j = 1
        o = True
        self.assertEqual(s.containsNearbyDuplicate(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,1,2,3]
        j = 2
        o = False
        self.assertEqual(s.containsNearbyDuplicate(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)