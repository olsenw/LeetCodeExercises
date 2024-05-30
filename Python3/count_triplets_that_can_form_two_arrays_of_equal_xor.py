# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr.

    Select three indices i, j and k where (0 <= i < j <= k < arr.length).

    Define a and b as follows:
    * a = arr[i] ^ arr[i+1] ^ ... ^ arr[j-1]
    * b = arr[j] ^ arr[j+1] ^ ... ^ arr[k]

    Note that ^ denotes the bitwise-xor operation.

    Return the number of triplets (i, j and k) where a == b.
    '''
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        n = len(arr)
        for i in range(n):
            x = arr[i]
            for j in range(i+1,n):
                x ^= arr[j]
                if x == 0:
                    answer += j - i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,1,6,7]
        o = 4
        self.assertEqual(s.countTriplets(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1,1]
        o = 10
        self.assertEqual(s.countTriplets(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)