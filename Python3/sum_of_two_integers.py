# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers a and b, return the sum of the two integers without using
    the operators + and -.
    '''
    # failing and incorrect
    def getSum_fails(self, a: int, b: int) -> int:
        answer = 0
        carry = 0
        for i in range(32):
            z = 1 << i
            x = a & z
            y = b & z
            if x == y == 0:
                answer |= carry
                carry = 0
            elif x == y == z:
                answer |= carry
                carry = 1 << (i+1)
            elif carry:
                carry = 1 << (i+1)
            else:
                answer |= 1 << i
                carry = 0
        return answer | carry

    # based on stack overflow
    # https://stackoverflow.com/questions/4068033/add-two-integers-using-only-bitwise-operators
    # works on positive numbers stuck on negative
    def getSum_closer(self, a: int, b: int) -> int:
        if a != b and abs(a) == abs(b):
            return 0
        carry = a & b
        result = a ^ b
        while carry:
            shift = carry << 1
            carry = result & shift
            result ^= shift
        a,b = min(a,b), max(a,b)
        if a < 0 and abs(a) > abs(b):
            return -result
        return result

    # based on Leetcode solution by Chirag Yadav
    # https://leetcode.com/problems/sum-of-two-integers/solutions/6913543/sum-of-two-integers-bitwise-carry-simulation-beats-100/
    # similar to above but with masking (artificially convert python int to 32 bit int)
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask
        MASK = 0xFFFFFFFF
        # maximum possible positive 32 bit int
        MAX = 0x7FFFFFFF
        # add carry to result until no more carry bits
        while b != 0:
            # shift all the bits that carry
            shift = (a & b) << 1
            # add stuff
            a = (a ^ b) & MASK
            # update carry bits for next round
            b = shift & MASK
        # convert the fixed bits back to python stuff
        return a if a <= MAX else ~(a ^ MASK)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 2
        o = 3
        self.assertEqual(s.getSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 3
        o = 5
        self.assertEqual(s.getSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = -6
        j = 3
        o = -3
        self.assertEqual(s.getSum(i,j), o)

    def test_four(self):
        s = Solution()
        i = -10
        j = 4
        o = -6
        self.assertEqual(s.getSum(i,j), o)

    def test_five(self):
        s = Solution()
        i = -1
        j = 1
        o = 0
        self.assertEqual(s.getSum(i,j), o)

    def test_six(self):
        s = Solution()
        i = -2
        j = 2
        o = 0
        self.assertEqual(s.getSum(i,j), o)

    def test_seven(self):
        s = Solution()
        i = -2
        j = 1
        o = -1
        self.assertEqual(s.getSum(i,j), o)

    def test_eight(self):
        s = Solution()
        i = -1
        j = -1
        o = -2
        self.assertEqual(s.getSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)