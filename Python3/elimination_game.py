# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list arr of all integers in the range [1,n] sorted in a strictly
    increasing order. Apply the following algorithm on arr:
    * Starting from left to right, remove the first number and every other
      number afterward until the end of list is reached.
    * Repeat the previous step again, but this time from right to left, remove
      the rightmost number and every other number from the remaining numbers.
    * Keep repeating the steps again, alternating left to right and right to
      left, until a single number remains.
    
    Given the integer n, return the last number remains in arr.
    '''
    # hits the memory limit
    def lastRemaining_memory_exceeded(self, n: int) -> int:
        arr = list(range(1,n+1))
        while len(arr) > 1:
            arr = [a for a in arr[1::2]][::-1]
            pass
        return arr[0]

    # just wrong
    def lastRemaining_fail(self, n: int) -> int:
        i = 1
        while n // i > 1:
            i *= 2
        return i

    # based on editorial by Loginov Kirill
    # https://leetcode.com/problems/elimination-game/solutions/6641901/unlock-the-recursive-elimination-pattern-for-last-remaining-number/?envType=problem-list-v2&envId=ng5yboc7
    def lastRemaining(self, n: int) -> int:
        # head is the current first element
        # step is the difference between elements
        # count is the number of elements remaining in the sequence
        # direction is which direction elements should be removed
        def r(head:int, step:int, count:int, direction:bool):
            if count == 1:
                return head
            if direction == True or count % 2 == 1:
                head += step
            return r(head, 2 * step, count // 2, not direction)
        return r(1, 1, n, True)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 9
        o = 6
        self.assertEqual(s.lastRemaining(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.lastRemaining(i), o)

    def test_three(self):
        s = Solution()
        i = 11
        o = 8
        self.assertEqual(s.lastRemaining(i), o)

    def test_four(self):
        s = Solution()
        i = 3
        o = 2
        self.assertEqual(s.lastRemaining(i), o)

    def test_five(self):
        s = Solution()
        i = 100000
        o = 55286
        self.assertEqual(s.lastRemaining(i), o)

    def test_six(self):
        s = Solution()
        i = 1000001
        o = 481110
        self.assertEqual(s.lastRemaining(i), o)

    def test_seven(self):
        s = Solution()
        i = 1000002
        o = 481112
        self.assertEqual(s.lastRemaining(i), o)

    def test_eight(self):
        s = Solution()
        i = 1000003
        o = 481112
        self.assertEqual(s.lastRemaining(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)