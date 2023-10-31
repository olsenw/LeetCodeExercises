# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array pref of size n. Find and return the array arr of size
    n that satisfies:
    * pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]

    Note that ^ denotes the bitwise-xor operation.

    The answer can be proven to be unique.
    '''
    def findArray_incorrect(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        running = pref[0]
        for p in pref[1:]:
            answer.append(running ^ p)
            running ^= answer[-1]
        return answer

    def findArray(self, pref: List[int]) -> List[int]:
        answer = []
        for i in range(len(pref) - 2, -1, -1):
            answer.append(pref[i] ^ pref[i+1])
        answer.append(pref[0])
        return answer[::-1] 

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,0,3,1]
        o = [5,7,2,3,2]
        self.assertEqual(s.findArray(i), o)

    def test_two(self):
        s = Solution()
        i = [13]
        o = [13]
        self.assertEqual(s.findArray(i), o)

    def test_three(self):
        s = Solution()
        i = [10, 2, 9, 5, 7, 3, 7, 5, 5, 8, 6, 7, 6, 5, 6, 2, 1, 5, 9, 5]
        o = [10,8,11,12,2,4,4,2,0,13,14,1,1,3,3,4,3,4,12,12]
        self.assertEqual(s.findArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)