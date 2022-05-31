# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import combinations_with_replacement

class Solution:
    '''
    Given a binary string s and an integer k, return true if every
    binary code of length k is a substring of s. Otherwise return false.
    '''
    # slow
    def hasAllCodes_hash_table(self, s: str, k: int) -> bool:
        codes = ['0', '1']
        for _ in range(1,k):
            update = []
            for c in codes:
                update.append(c + '0')
                update.append(c + '1')
            codes = update
        d = {c:False for c in codes}
        for i in range(len(s) - k + 1):
            d[s[i:i+k]] = True
        return all(d.values())

    # based on observing the fact that there are 2^k possible codes
    def hasAllCodes_set(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s) - k + 1):
            codes.add(s[i:i+k])
        return len(codes) == 2 ** k

    # rolling hash idea from leetcode solutions
    # https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solution/
    # rolling hash works because each binary string is a unique number
    # so by doing bit manipulation it is possible to update hash quickly
    # use an array to mark found hashes
    def hasAllCodes(self, s: str, k: int) -> bool:
        target = 2 ** k # alternatively 1 << k
        ones = target - 1 # binary ones length k
        found = [False] * target # basically a set for all codes
        h = int(s[0:k],2) # rolling hash (initialized with first code)
        found[h] = True
        target -= 1
        for i in range(k,len(s)):
            # update hash with next element
            h = ((h << 1) & ones) | int(s[i])
            if not found[h]:
                found[h] = True
                target -= 1
                # early cutout (found all possible codes)
                if target == 0:
                    return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "00110110"
        j = 2
        o = True
        self.assertEqual(s.hasAllCodes(i, j), o)

    def test_two(self):
        s = Solution()
        i = "0110"
        j = 1
        o = True
        self.assertEqual(s.hasAllCodes(i, j), o)

    def test_three(self):
        s = Solution()
        i = "0110"
        j = 2
        o = False
        self.assertEqual(s.hasAllCodes(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)