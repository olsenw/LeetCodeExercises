# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array complexity of length n.

    There are n locked computers in a room with labels from 0 to n - 1, each
    with its own unique password. The password of the computer i has a
    complexity complexity[i].

    The password for the computer labeled 0 is already decrypted and serves as
    the root. All other computers must be unlocked using it or another
    previously unlocked computer, following this information:
    * The password for computer i can be decrypted using the password for j,
      where j is any integer less than i with a lower complexity. (ie j < i and 
      complexity[j] < complexity[i])
    * To decrypt the password for computer i, the password for computer j must
      already decrypted such that j < i and complexity[j] < complexity[i].

    Find the number of permutations of [0, 1, 2, ..., n - 1] that represents a
    valid order in which the computers can be unlocked, starting from computer 0
    as the only initially unlocked one.

    Since the answer may be large, return it modulo 10^9 + 7.

    Note that the password for the computer with label 0 is decrypted, and not
    the computer with the first position in the permutation.
    '''
    # based on hints
    def countPermutations(self, complexity: List[int]) -> int:
        m = complexity.count(complexity[0])
        if m > 1 or min(complexity) != complexity[0]:
            return 0
        return math.factorial(len(complexity) - 1) % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 2
        self.assertEqual(s.countPermutations(i), o)

    def test_two(self):
        s = Solution()
        i = [3,3,3,4,4,4]
        o = 0
        self.assertEqual(s.countPermutations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)