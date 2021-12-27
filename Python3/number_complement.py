# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) + 1
        # print()
        # print(format(num, 'b'))
        # print(format(mask, 'b'))
        # print(format(num ^ mask, 'b'))
        return num ^ mask
        
        # slower by ~4ms
        # return num ^ ((1 << num.bit_length()) - 1)

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.findComplement(5), 2)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.findComplement(1), 0)

    def test_three(self):
        s = Solution()
        # 78541200  =>  100 1010 1110 0111 0001 1001 0000
        # 55676527  =>   11 0101 0001 1000 1110 0110 1111
        self.assertEqual(s.findComplement(78541200), 55676527)

    def test_four(self):
        s = Solution()
        # 2147483648  =>  1000 0000 0000 0000 0000 0000 0000 0000
        # 2147483647  =>   111 1111 1111 1111 1111 1111 1111 1111
        self.assertEqual(s.findComplement(2147483648), 2147483647)

    def test_five(self):
        s = Solution()
        # 2147483647  =>  111 1111 1111 1111 1111 1111 1111 1111
        # 0           =>  000 0000 0000 0000 0000 0000 0000 0000
        self.assertEqual(s.findComplement(2147483647), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)