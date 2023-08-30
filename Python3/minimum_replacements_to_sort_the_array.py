# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. In one operation it is possible to
    replace any element of the array with any two elements that sum to it.

    Return the minimum number of operations to make an array that is sorted in
    non-decreasing order.
    '''
    def minimumReplacement_fails(self, nums: List[int]) -> int:
        answer = 0
        b = nums[-1]
        while nums:
            c = nums.pop()
            if c > b:
                answer += 1
                if c % b == 0:
                    nums.append(b)
                    nums.append(c-b)
                elif c % 2:
                    nums.append(c // 2)
                    nums.append(c // 2 + 1)
                else:
                    nums.append(c // 2)
                    nums.append(c // 2)
                b = min(b, nums[-1])
            b = min(b,c)
        return answer

    def minimumReplacement_fails2(self, nums: List[int]) -> int:
        answer = 0
        b = nums[-1]
        while nums:
            c = nums.pop()
            if c > b:
                answer += 1
                nums.append(c-b)
                nums.append(b)
                b = min(b, nums[-1])
        return answer

    def minimumReplacement_fails3(self, nums: List[int]) -> int:
        answer = 0
        b = nums[-1]
        while nums:
            while len(nums) > 1:
                c = nums.pop()
                if c > b:
                    answer += 1
                    split = c // 2
                    if split > b:
                        nums.append(c - b)
                        nums.append(b)
                    elif c % 2:
                        nums.append(c // 2 + 1)
                        nums.append(c // 2)
                    else:
                        nums.append(c // 2)
                        nums.append(c // 2)
                    b = min(b, nums[-1])
            c = nums.pop()
            if c > b:
                answer += 1
                split = c // 2
                if split > b:
                    nums.append(b)
                    nums.append(c - b)
                elif c % 2:
                    nums.append(c // 2)
                    nums.append(c // 2 + 1)
                else:
                    nums.append(c // 2)
                    nums.append(c // 2)
                b = min(b, nums[-1])
        return answer

    # working with the editorial
    # https://leetcode.com/problems/minimum-replacements-to-sort-the-array/submissions/
    # played myself by trying to be fancy with while and pop
    def minimumReplacement(self, nums: List[int]) -> int:
        correct = nums.copy()
        n = len(nums)
        answer = 0
        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if correct[i] <= correct[i + 1]:
                continue
            
            # Count how many elements are made from breaking nums[i].
            num_elements = (correct[i] + correct[i + 1] - 1) // correct[i + 1]
            
            # It requires numElements - 1 replacement operations.
            answer += num_elements - 1

            # Maximize nums[i] after replacement.
            correct[i] = correct[i] // num_elements
        correct.reverse()

        answer = 0
        b = nums[-1]
        bad = []
        while nums:
            c = nums.pop()
            if c > b:
                e = (c + b - 1) // b
                answer += e - 1
                b = c // e
            bad.append(b)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,9,3]
        o = 2
        self.assertEqual(s.minimumReplacement(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.minimumReplacement(i), o)

    def test_three(self):
        s = Solution()
        i = [5,4,3,2,1]
        o = 10
        self.assertEqual(s.minimumReplacement(i), o)

    def test_four(self):
        s = Solution()
        i = [3,10,3]
        o = 4
        self.assertEqual(s.minimumReplacement(i), o)

    def test_five(self):
        s = Solution()
        i = [84, 49, 8, 80, 6, 56, 14, 57, 35, 38, 87, 6, 91, 56, 67, 9, 18, 70, 82, 32, 62, 89, 46, 5, 86, 33, 95, 71, 36, 91, 61, 95, 30, 69, 99, 75, 55, 59, 23, 43, 21, 56, 19, 92, 99, 51, 44, 98, 62, 60, 31, 31, 86, 17, 22, 9, 69, 5, 49, 84, 24, 30, 10, 21, 6, 7, 91, 61, 19, 67, 4, 14, 9, 26, 41, 52, 53, 25, 39, 19, 46, 76, 32, 55, 37, 88, 14, 63, 8, 31, 37, 48, 80, 88, 63, 11, 65, 31, 68, 38]
        o = 4034
        self.assertEqual(s.minimumReplacement(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)