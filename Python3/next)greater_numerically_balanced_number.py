# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An integer x is numerically balanced if for every digit d in the number x,
    there are exactly d occurrences of that digit in x.

    Given an integer n, return the smallest numerically balanced number strictly
    greater than n.
    '''
    # brute force
    def nextBeautifulNumber_brute(self, n: int) -> int:
        def balanced(test: int) -> bool:
            c = Counter(str(test))
            return all(c[i] == int(i) for i in c)
        x = n+1
        while not balanced(x):
            x += 1
        return x

    # for given input range there are 110 balanced numbers
    # pre generated all of them and do a bisect
    def nextBeautifulNumber(self, n: int) -> int:
        # used to generate all possible answers
        # def balanced(test: int) -> bool:
        #     c = Counter(str(test))
        #     return all(c[i] == int(i) for i in c)
        # possible = [i for i in range(1,1224445) if balanced(i)]
        possible = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133, 223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123, 233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123, 332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551, 666666, 1224444]
        i = bisect.bisect(possible, n)
        return possible[i]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 22
        self.assertEqual(s.nextBeautifulNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 1000
        o = 1333
        self.assertEqual(s.nextBeautifulNumber(i), o)

    def test_three(self):
        s = Solution()
        i = 3000
        o = 3133
        self.assertEqual(s.nextBeautifulNumber(i), o)

    def test_four(self):
        s = Solution()
        i = 1000000
        o = 1224444
        self.assertEqual(s.nextBeautifulNumber(i), o)

    def test_five(self):
        s = Solution()
        i = 999
        o = 1333
        self.assertEqual(s.nextBeautifulNumber(i), o)

    def test_six(self):
        s = Solution()
        i = 233320
        o = 233321
        self.assertEqual(s.nextBeautifulNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)