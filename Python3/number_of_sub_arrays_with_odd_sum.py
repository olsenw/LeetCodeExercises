# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, return the number of subarrays with an odd
    sum.

    Since the answer can be very large, return it modulo 10^9 + 7.
    '''
    # does not count cases of even and odd subarrays
    def numOfSubarrays_wrong(self, arr: List[int]) -> int:
        answer = 0
        even = 0
        odd = 0
        for a in arr:
            if a % 2:
                odd += 1
                answer += 1 + even
            else:
                even += 1
                answer += odd
        return answer 

    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        even = 0
        odd = 0
        running = 0
        for a in arr:
            running += a
            if running % 2:
                odd += 1
                answer += 1 + even
            else:
                even += 1
                answer += odd
        return answer % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5]
        o = 4
        self.assertEqual(s.numOfSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [2,4,6]
        o = 0
        self.assertEqual(s.numOfSubarrays(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6,7]
        o = 16
        self.assertEqual(s.numOfSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)