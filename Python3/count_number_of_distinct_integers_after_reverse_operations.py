# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums consisting of positive integers.

    Take each integer in the array, reverse its digits, and add it to the end of
    the array. This operation should only be applied to the original integers in
    nums.

    Return the number of distinct integers in the final array.
    '''
    # solved wrong problem...
    def countDistinctIntegers_oops(self, nums: List[int]) -> int:
        # this is incorrect... math error
        def reverse(i:int) -> int:
            a = 0
            while i:
                a += i % 10
                i //= 10
            return a
        many = set()
        once = set()
        def account(nums:List[int]) -> None:
            for n in nums:
                if n in many:
                    continue
                elif n in once:
                    many.add(n)
                    once.remove(n)
                else:
                    once.add(n)
        account(nums)
        account([reverse(n) for n in once])
        return len(once)

    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(i:int) -> int:
            a = 0
            while i:
                a = a * 10 + i % 10
                i //= 10
            return a
        nums = set(nums)
        nums.update([reverse(n) for n in nums])
        return len(nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,13,10,12,31]
        o = 6
        self.assertEqual(s.countDistinctIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2]
        o = 1
        self.assertEqual(s.countDistinctIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)