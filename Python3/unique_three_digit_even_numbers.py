# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of digits called digits. Determine the number of distinct
    three-digit even numbers that can be formed using these digits.

    Note: Each copy of a digit can only be used once per number, and there may
    not be leading zeros.
    '''
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        answer = set()
        for i in range(n):
            a = digits[i] * 100
            for j in range(n):
                if i != j:
                    b = a + digits[j] * 10
                    for k in range(n):
                        if i != k and j != k and b > 99 and digits[k] % 2 == 0:
                            answer.add(b + digits[k])
        return len(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 12
        self.assertEqual(s.totalNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [0,2,2]
        o = 2
        self.assertEqual(s.totalNumbers(i), o)

    def test_three(self):
        s = Solution()
        i = [6,6,6]
        o = 1
        self.assertEqual(s.totalNumbers(i), o)

    def test_four(self):
        s = Solution()
        i = [1,3,5]
        o = 0
        self.assertEqual(s.totalNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)