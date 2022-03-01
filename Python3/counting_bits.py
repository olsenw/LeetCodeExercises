# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, return an array ans of length n+1 such that for
    each i (0 <= i <= n), ans[i] is the number of 1's in the binary
    representation of i.
    '''
    # O(n log2 n) time (n iterations on log2 n length strings)
    def countBits_brute(self, n: int) -> List[int]:
        # log2 n
        def count(n):
            c = 0
            for s in bin(n)[2:]:
                c += ord(s) - ord('0')
            return c
        # n
        return [count(i) for i in range(n+1)]

    def countBits(self, n: int) -> List[int]:
        bits = [0,1]
        # 2 -> 4 -> 8 -> 16 -> ... 
        while len(bits) <= n:
            bits += [1 + i for i in bits]
        return bits[:n+1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = [0,1,1]
        self.assertEqual(s.countBits_brute(i), o)
        self.assertEqual(s.countBits(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = [0,1,1,2,1,2]
        self.assertEqual(s.countBits_brute(i), o)
        self.assertEqual(s.countBits(i), o)

    def test_three(self):
        s = Solution()
        i = 8
        o = [0,1,1,2,1,2,2,3,1]
        self.assertEqual(s.countBits_brute(i), o)
        self.assertEqual(s.countBits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # for i, j in enumerate(Solution().countBits_brute(20)):
    #     print(f"{i}->{j}\t{bin(i)}")