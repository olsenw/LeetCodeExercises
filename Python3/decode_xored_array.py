# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a hidden integer array arr that consists of n non-negative
    integers.

    It was encoded into another integer array encoded of length n - 1, such that
    encoded[i] = arr[i] XOR arr[i+1].

    Given the encoded array and an integer first, that is the first element of
    arr, return the original array arr.
    '''
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for n in encoded:
            # xor operatior is ^
            answer.append(answer[-1] ^ n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = 1
        o = [1,0,2,1]
        self.assertEqual(s.decode(i,j), o)

    def test_two(self):
        s = Solution()
        i = [6,2,7,3]
        j = 4
        o = [4,2,0,7,4]
        self.assertEqual(s.decode(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)