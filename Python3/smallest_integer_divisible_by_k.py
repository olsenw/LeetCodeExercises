# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a positive integer k, find the length of the smallest positive
    integer n such that n is divisible by k, and n is comprised only by
    the digit 1.

    Return the length of n. If there is no such n, return -1.

    Note: n may not fit in a 64-bit signed integer.
    1 <= k <= 10^5
    '''
    def smallestRepunitDivByK_brute(self, k: int) -> int:
        # cannot be an even number (always ends 0,2,4,6,8)
        # cannot be multiple of five (always ends 0,5)
        if k % 2 == 0 or k % 5 == 0:
            return -1
        n = 1
        c = 1
        while n % k != 0:
            n = n * 10 + 1
            c += 1
        return c

    '''
    based on solution from leetcode
    note that there can only be k possible remainders before repeating
    '''
    def smallestRepunitDivByK_smarter(self, k: int) -> int:
        # this check actually slows this down according to testing...
        # if k % 2 == 0 or k % 5 == 0:
        #     return -1
        r = 0
        '''
        Only check k remainders because of the Pigeonhole
        principle.

        ie there are only k possible remainders and if we repeat then
        already past least sized n
        '''
        for i in range(1, k+1):
            # fancy remainder math to stay within the bounds of an int
            # allowed because n and r would have same remainders of k
            r = (r * 10 + 1) % k
            if r == 0:
                return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = -1
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

    def test_four(self):
        s = Solution()
        i = 5
        o = -1
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

    def test_five(self):
        s = Solution()
        i = 7
        o = 6
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

    def test_six(self):
        s = Solution()
        i = 9981
        o = 9972
        self.assertEqual(s.smallestRepunitDivByK_brute(i), o)
        self.assertEqual(s.smallestRepunitDivByK_smarter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    '''
    code to brute force all the answers
    '''
    # s = Solution()
    # k = 10**5
    # l = [i for i in range(k) if i % 2 != 0 and i % 5 != 0]
    # n = [s.smallestRepunitDivByK(i) for i in l]
    # m = max(n)
    # i = n.index(m)
    # print(f'{l[i]:>5}', "(", i, ")", " -> ", m)
    # with open('smallest_integer_divisible_by_k_crunch.txt', 'a') as f:
    #     f.write("{0:5} -> {1}\n".format(l[i], m))
    #     f.write("---------------------------------------------------")
    #     for i in range(len(l)):
    #         f.write("{0:5} -> {1}\n".format(l[i], n[i]))
