# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A subarray is called balanced if the number of distinct even numbers in the
    subarray is equal to the number of distinct odd numbers.

    Return the length of the longest balanced subarray.
    '''
    # passes 985 of 999 cases
    def longestBalanced_tle(self, nums: List[int]) -> int:
        answer = 0
        c = Counter()
        for i in range(len(nums)):
            c[nums[i]] += 1
            t = Counter(c)
            for j in range(i):
                pass
                if len(t) % 2 == 0 and sum(k % 2 for k in t) == len(t) // 2:
                    answer = max(answer, i - j + 1)
                t[nums[j]] -= 1
                if t[nums[j]] == 0:
                    del t[nums[j]]
        return answer

    def longestBalanced(self, nums: List[int]) -> int:
        answer = 0
        c = Counter()
        e,o = 0,0
        for i in range(len(nums)):
            c[nums[i]] += 1
            t = Counter()
            if c[nums[i]] == 1:
                if nums[i] % 2:
                    o += 1
                else:
                    e += 1
            a,b = e,o
            for j in range(i):
                if a == b:
                    answer = max(answer, i - j + 1)
                t[nums[j]] += 1
                if t[nums[j]] == c[nums[j]]:
                    if nums[j] % 2:
                        b -= 1
                    else:
                        a -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,4,3]
        o = 4
        self.assertEqual(s.longestBalanced(i), o)

    def test_two(self):
        s = Solution()
        i = [3,2,2,5,4]
        o = 5
        self.assertEqual(s.longestBalanced(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,2]
        o = 3
        self.assertEqual(s.longestBalanced(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)