# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n indicating there are n specialty retail stores. There are
    m product types of varying amounts, which are given as a 0-indexed integer
    array quantities, where quantities[i] represents the number of products of
    the ith product type.

    Distribute all products to the retail stores following these rules:
    * A store can only be given at most one product type but can be given any
      amount of it.
    * After distribution, each store will have been given some number of
      products (possibly 0). Let x represent the maximum number of products
      given to any store. x should be as small as possible.
    
    Return the minimum possible x.
    '''
    def minimizedMaximum_fails(self, n: int, quantities: List[int]) -> int:
        # def test(target):
        #     t = n
        #     for q in quantities:
        #         t -= q // target
        #         if q % target:
        #             t -= 1
        #     return t <= 0
        def test(target):
            i = 0
            j = 0
            while i < len(quantities):
                j += math.ceil(quantities[i] / target)
                if j >= n:
                    return True
                i += 1
            return False
        a,b = 0, max(quantities)
        while a <= b:
            c = a + (b - a) // 2
            if not test(c):
                b = c - 1
            else:
                a = c + 1
        return b

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def test(target):
            t = 0
            for q in quantities:
                a,b = divmod(q, target)
                t += a
                if b:
                    t += 1
                if t > n:
                    return False
            return True
        a,b = 1, max(quantities)
        while a < b:
            c = a + (b - a) // 2
            t = test(c)
            if t:
                b = c
            else:
                a = c + 1
        return b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [11,6]
        o = 3
        self.assertEqual(s.minimizedMaximum(i,j), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = [15,10,10]
        o = 5
        self.assertEqual(s.minimizedMaximum(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = [100000]
        o = 100000
        self.assertEqual(s.minimizedMaximum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)