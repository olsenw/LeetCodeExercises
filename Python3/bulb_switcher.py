# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n bulbs that are initially off. In the first round all the bulbs
    are turned on. During the second round every second bulb is turned off. On
    the third round every third bulb is toggled to the opposite state. This
    pattern continues for subsequent rounds with the nth round only toggling the
    nth bulb.

    Return the number of bulbs that are on after n rounds.
    '''
    # O(n^2) time (time limit exceeded)
    def bulbSwitch_brute(self, n: int) -> int:
        if n == 0:
            return 0
        # bulbs = [True] * n
        bulbs = [1] * n
        print()
        print(bulbs)
        for i in range(2, n+1):
            for j in range(i - 1, n, i):
                # bulbs[j] = not bulbs[j]
                bulbs[j] = 0 if bulbs[j] else 1
            print(bulbs)
        print()
        return sum(bulbs)

    def bulbSwitch_correct(self, n: int) -> int:
        answer = 0
        i = 1
        j = 2
        while i <= n:
            answer += 1
            i += j + 1
            j += 2
        return answer

    # reading leetcode editorial pointed out that the solution is just the
    # square root of the number of bulbs...
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = 1
        self.assertEqual(s.bulbSwitch(i), o)

    def test_two(self):
        s = Solution()
        i = 0
        o = 0
        self.assertEqual(s.bulbSwitch(i), o)

    def test_three(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.bulbSwitch(i), o)

    def test_four(self):
        s = Solution()
        i = 2
        o = 1
        self.assertEqual(s.bulbSwitch(i), o)

    def test_five(self):
        s = Solution()
        i = 4
        o = 2
        self.assertEqual(s.bulbSwitch(i), o)

    def test_six(self):
        s = Solution()
        i = 100
        o = 10
        self.assertEqual(s.bulbSwitch(i), o)

    def test_seven(self):
        s = Solution()
        i = 10000
        o = 100
        self.assertEqual(s.bulbSwitch(i), o)

    def test_eight(self):
        s = Solution()
        i = 10
        o = 3
        self.assertEqual(s.bulbSwitch(i), o)

    def test_nine(self):
        s = Solution()
        i = 30
        o = 5
        self.assertEqual(s.bulbSwitch(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)