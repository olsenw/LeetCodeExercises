# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import permutations
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The XOR total of an array is defined as the bitwise XOR of all its elements,
    or 0 if the array is empty.

    Given an array nums, return the sum of all XOR totals for every subset of
    nums.

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by deleting
    some (possible zero) elements of b.
    '''
    # only accounts for continuous subsets
    def subsetXORSum_fails(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            x = 0
            for j in range(i, n):
                x ^= nums[j]
                answer += x
        return answer

    # Leetcode editorial backtracking solution
    # https://leetcode.com/problems/sum-of-all-subset-xor-totals/editorial/?envType=daily-question&envId=2024-05-20
    # uses backtracking to generate all subsets
    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(nums, index, subset, subsets):
            # Base case: index reached end of nums
            # Add the current subset to subsets
            if index == len(nums):
                subsets.append(subset[:])
                return

            # Generate subsets with nums[i]
            subset.append(nums[index])
            generate_subsets(nums, index + 1, subset, subsets)
            subset.pop()

            # Generate subsets without nums[i]
            generate_subsets(nums, index + 1, subset, subsets)

        # Generate all of the subsets
        subsets = []
        generate_subsets(nums, 0, [], subsets)

        # Compute the XOR total for each subset and add to the result
        result = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total

        return result

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3]
        o = 6
        self.assertEqual(s.subsetXORSum(i), o)

    def test_two(self):
        s = Solution()
        i = [5,1,6]
        o = 28
        self.assertEqual(s.subsetXORSum(i), o)

    def test_three(self):
        s = Solution()
        i = [3,4,5,6,7,8]
        o = 480
        self.assertEqual(s.subsetXORSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)