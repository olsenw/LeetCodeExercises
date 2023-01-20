# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return all the different possible
    non-decreasing subsequences of the given array with at least two elements.
    '''
    # finds all subarrays not subsequences
    def findSubsequences_incorrect(self, nums: List[int]) -> List[List[int]]:
        answer = []
        run = [[nums[0]]]
        for j in range(1, len(nums)):
            if nums[j - 1] > nums[j]:
                run = [[nums[j]]]
            else:
                run = [r + [nums[j]] for r in run]
                answer.extend(run)
                run.append([nums[j]])
        return answer

    # backtracking nightmare
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        @cache
        def r(i:int):
            # if len(nums) == 0:
                # return []
            if i == len(nums) - 1:
                return []
            answer = []
            n = set()
            for j in range(i+1,len(nums)):
                if nums[j] not in n and nums[i] <= nums[j]:
                    n.add(nums[j])
                    answer.append([nums[i], nums[j]])
                    answer.extend([nums[i]] + r for r in r(j))
            return answer
        answer = []
        n = set()
        for i in range(len(nums) - 1):
            if nums[i] not in n:
                n.add(nums[i])
                answer.extend(r(i))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,6,7,7]
        o = [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        self.assertEqual(sorted(s.findSubsequences(i)), o)

    def test_two(self):
        s = Solution()
        i = [4,4,3,2,1]
        o = [[4,4]]
        self.assertEqual(sorted(s.findSubsequences(i)), o)

    def test_three(self):
        s = Solution()
        i = [4,4,4]
        o = [[4,4], [4,4,4]]
        self.assertEqual(sorted(s.findSubsequences(i)), o)

    def test_four(self):
        s = Solution()
        i = [3,2,1]
        o = []
        self.assertEqual(sorted(s.findSubsequences(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)