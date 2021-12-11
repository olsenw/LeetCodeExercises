# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A positive integer is magical if it is divisible by either a or b.

    Given the three integers n, a, and b, return the nth magical number.

    Return it modulo 10**9+7
    '''
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        modulo = 10**9+7
        lcm = math.lcm(a, b)
        magicLcm = lcm // a + lcm // b - 1
        found, left = divmod(n, magicLcm)
        if left == 0:
             return (found * lcm) % modulo
        aMult = (found * lcm) % modulo
        bMult = (found * lcm) % modulo
        # print(n, a, b, lcm, magicLcm, found, left, aMult, bMult)
        for i in range(found * magicLcm, n + 1):
            # print(aMult, bMult)
            if aMult <= bMult:
                aMult += a % modulo
            else:
                bMult += b % modulo
        return min(aMult, bMult) % modulo

'''
This works be finding the repeating pattern and brute forcing the
remaining magic numbers.

The lowest common multiple of a and b is when the pattern of magic
numbers repeats itself. The number of magic numbers in this section of
the pattern is (lcm / a) + (lcm / b) - 1 (note: -1 needed for lcm which a and
b share). You can use this to calculate the repeating pattern of magic
numbers and then increment from there to find the magic numbers in the
remianing segment.

number line showing magic numbers marked by divisible by a=2 and b=3
1   2   3   4   5   6  |  7   8   9   10  11  12
    a   b   a       ab |      a   b   a       ab
                       | pattern repeats ->
'''

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.nthMagicalNumber(1, 2, 3), 2)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.nthMagicalNumber(4, 2, 3), 6)

    def test_three(self):
        s = Solution()
        self.assertEqual(s.nthMagicalNumber(5, 2, 4), 10)

    def test_four(self):
        s = Solution()
        self.assertEqual(s.nthMagicalNumber(3, 6, 4), 8)

if __name__ == '__main__':
    unittest.main(verbosity=2)