# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D array queries, where queries[i] is of the form [l, r]. Each
    queries[i] defines an array of integers nums consisting of elements ranging
    from l to r, both inclusive.

    In operation it is possible to:
    * Select two integers a and b from the array.
    * Replace them with floor(a / 4) and floor(b / 4).

    Determine the minimum number of operations required to reduce the all
    elements of the array to zero for each query. Return the sum of the results
    for all queries.
    '''
    # slow O(n * m)
    # n number of queries
    # m maximum range of a query
    def minOperations_brute(self, queries: List[List[int]]) -> int:
        def operations(l:int, r:int) -> int:
            c = Counter()
            # hint 2
            for i in range(r,l-1,-1):
                # hint 1
                j = math.floor(math.log(i,4))+1
                c[j] += 1
            test = 0
            r = 0
            for i in c:
                test += (i * c[i]) // 2
                r += (i * c[i]) % 2
            return test + r // 2 + r % 2
        answer = 0
        for l,r in queries:
            answer += operations(l,r)
        return answer

    def minOperations(self, queries: List[List[int]]) -> int:
        def operations(l:int, r:int) -> int:
            a,b = 0,0
            c = Counter()
            for i in range(15):
                x,y = 4**i, 4**(i+1) - 1
                if x <= l < r <= y:
                    c[i+1] = r - l + 1
                elif x <= l <= y < r:
                    c[i+1] = y - l + 1
                elif l < x <= r <= y: 
                    c[i+1] = r - x + 1
                elif l < x < y < r:
                    c[i+1] = y - x + 1
            # d = Counter()
            # # hint 2
            # for i in range(r,l-1,-1):
            #     # hint 1
            #     j = math.floor(math.log(i,4))+1
            #     d[j] += 1
            # if c != d:
            #     pass
            for i in c:
                a += (i * c[i]) // 2
                b += (i * c[i]) % 2
            return a + b // 2 + b % 2
        return sum(operations(l,r) for l,r in queries)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,4]]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,6]]
        o = 4
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [[10,20],[100,200],[1000,2000],[20000,40000],[100000,200000]]
        o = 533216
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [[100,200]]
        o = 202
        self.assertEqual(s.minOperations(i), o)

    def test_five(self):
        s = Solution()
        i = [[16,22],[2,15]]
        o = 24
        self.assertEqual(s.minOperations_brute(i), o)
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)