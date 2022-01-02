# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a list of songs where the ith song has a duration of time[i]
    seconds.

    Return the number of pairs of songs for which their total duration
    in seconds is divisible by 60.

    Formally: the number of indices i,j such that i < j with
    (time[i] + time[j]) % 60 == 0.
    '''
    # O(n) there can be 60 possible remainders, count then calc answer
    def problem_name(self, time: List[int]) -> int:
        # helper to do combinations w/o repetition
        def nr(n: int, r: int) -> int:
            if n < r: return 0
            import math
            return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
        # useful for auto initialization of dictionary values
        from collections import defaultdict
        d = defaultdict(int) # default is int(0)
        # turn times into remainder counts
        for t in time:
            d[t%60] += 1
        # handle special case of 0 remainder and 30 remainder
        pairs = nr(d[0], 2) + nr(d[30], 2)
        # handle other pairs
        for i in range(1,30):
            pairs += d[i] * d[60-i]
        return pairs

    # brute force O(n^2) just checks every pair
    def problem_name_brute(self, time: List[int]) -> int:
        pairs = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    pairs += 1
        return pairs

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [30,20,150,100,40]
        o = 3
        self.assertEqual(s.problem_name(i), o)
        self.assertEqual(s.problem_name_brute(i), o)

    def test_two(self):
        s = Solution()
        i = [60,60,60]
        o = 3
        self.assertEqual(s.problem_name(i), o)
        self.assertEqual(s.problem_name_brute(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)