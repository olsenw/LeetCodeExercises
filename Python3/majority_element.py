# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more tha [n/2]
    times. Test cases guarantee a majority element exists.
    '''
    def majorityElement_Counter(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

    def majorityElement_Dictionary(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for k in d:
            if d[k] > len(nums) // 2:
                return k

    # interesting idea saw in multiple discussion posts
    # https://leetcode.com/problems/majority-element/discuss/
    def majorityElement_Sort(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # similar idea to Sort but make use of min heap
    def majorityElement_Heapq(self, nums: List[int]) -> int:
        import heapq
        heapq.heapify(nums)
        for _ in range(len(nums) // 2):
            heapq.heappop(nums)
        return nums[0]

    # O(n) time O(1) space
    # based on discussion post by softray (was inspired by jojocat1010)
    # https://leetcode.com/problems/majority-element/discuss/51887/Python-O(n)-time-O(1)-space-two-simple-solutions
    def majorityElement_LinearConstant(self, nums: List[int]) -> int:
        n, c = nums[0], 1
        for num in nums[1:]:
            n, c = (n, c+1 if n == num else c-1) if c else (num, 1)
        return n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,3]
        o = 3
        self.assertEqual(s.majorityElement_Counter(i), o)
        self.assertEqual(s.majorityElement_Dictionary(i), o)
        self.assertEqual(s.majorityElement_Heapq(list(i)), o)
        self.assertEqual(s.majorityElement_Sort(list(i)), o)
        self.assertEqual(s.majorityElement_LinearConstant(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,1,1,1,2,2]
        o = 2
        self.assertEqual(s.majorityElement_Counter(i), o)
        self.assertEqual(s.majorityElement_Dictionary(i), o)
        self.assertEqual(s.majorityElement_Heapq(list(i)), o)
        self.assertEqual(s.majorityElement_Sort(list(i)), o)
        self.assertEqual(s.majorityElement_LinearConstant(i), o)

    def test_three(self):
        s = Solution()
        i = [3,3,4]
        o = 3
        self.assertEqual(s.majorityElement_Counter(i), o)
        self.assertEqual(s.majorityElement_Dictionary(i), o)
        self.assertEqual(s.majorityElement_Heapq(list(i)), o)
        self.assertEqual(s.majorityElement_Sort(list(i)), o)
        self.assertEqual(s.majorityElement_LinearConstant(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)