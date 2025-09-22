# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A self-dividing number is a number that is divisible by every digit in
    contains.

    A self-dividing number is not allowed to contain the digit zero.

    Given two integers left and right, return a list of all the self-dividing
    numbers in the range [left, right] (both inclusive).
    '''
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right + 1):
            if all(digit != '0' and num % int(digit) == 0 for digit in str(num)):
                answer.append(num)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 22
        o = [1,2,3,4,5,6,7,8,9,11,12,15,22]
        self.assertEqual(s.selfDividingNumbers(i,j), o)

    def test_two(self):
        s = Solution()
        i = 47
        j = 85
        o = [48,55,66,77]
        self.assertEqual(s.selfDividingNumbers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)