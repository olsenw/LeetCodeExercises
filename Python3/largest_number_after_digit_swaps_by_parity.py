# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer num. It is possible to swap any two digits of num
    that have the same parity (i.e. both odd digits or both even digits).

    Return the largest possible value of num after any number of swaps.
    '''
    def largestInteger(self, num: int) -> int:
        num = [int(c) for c in str(num)]
        even = [-n for n in num if n % 2 == 0]
        heapq.heapify(even)
        odd = [-n for n in num if n % 2 == 1]
        heapq.heapify(odd)
        answer = 0
        for n in num:
            answer *= 10
            if n % 2 == 1:
                answer -= heapq.heappop(odd)
            else:
                answer -= heapq.heappop(even)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1234
        o = 3412
        self.assertEqual(s.largestInteger(i), o)

    def test_two(self):
        s = Solution()
        i = 65875
        o = 87655
        self.assertEqual(s.largestInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)