# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    An integer is called Monobit if all bits in its binary representation are
    the same.

    Return the count of Monobit integers in the range [0, n] (inclusive).
    '''
    def countMonobit(self, n: int) -> int:
        answer = 1
        count = 1
        while count <= n:
            answer += 1
            count <<= 1
            count += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 2
        self.assertEqual(s.countMonobit(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = 3
        self.assertEqual(s.countMonobit(i), o)

    def test_three(self):
        s = Solution()
        i = 999
        o = 10
        self.assertEqual(s.countMonobit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)