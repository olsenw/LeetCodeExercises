# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, and three integers a, b, and c. Find the
    number of good triplets.

    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are
    true:
    * 0 <= i < j < k < arr.length
    * abs(arr[i] - arr[j]) <= a
    * abs(arr[j] - arr[k]) <= b
    * abs(arr[i] - arr[k]) <= c

    Return the number of good triplets.
    '''
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        answer = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (abs(arr[i] - arr[j]) <= a and 
                        abs(arr[j] - arr[k]) <= b and 
                        abs(arr[i] - arr[k]) <= c):
                        answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,0,1,1,9,7], 7, 2, 3
        o = 4
        self.assertEqual(s.countGoodTriplets(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,2,3], 0,0,1
        o = 0
        self.assertEqual(s.countGoodTriplets(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)