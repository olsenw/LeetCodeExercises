# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nuums, where it is allowed to traverse
    between indices. It is possible to traverse between index i and index j,
    i != j, if and only if gcd(nums[i], nums[j]) > 1 where gcd is the greatest
    common divisor.

    The task is to determine if for every pair of indices i and j in nums, where
    i < j, there exists a sequence of traversals that can be made from i to j.

    Return true if it is possible to traverse between all such pairs of indices,
    or false otherwise.
    '''
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if nums == [1]:
            return True
        factors = [Solution.primeFactors(n) for n in nums]
        graph = defaultdict(set)
        for s in factors:
            if not len(s):
                return False
            for x in s:
                for y in s:
                    # if x != y:
                        graph[x].add(y)
                        graph[y].add(x)
        l = len(graph)
        visited = set()
        q = set(factors[0])
        while q:
            n = q.pop()
            if n in visited:
                continue
            visited.add(n)
            q.update(graph[n])
        return len(visited) == l
    
    # prime factor copied from GeeksforGeeks
    # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
    # O(sqrt n) time and O(1) space
    def primeFactors(n:int)->Set[int]:
        answer = set()
        while n % 2 == 0:
            answer.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                answer.add(i)
                n //= i
        if n > 2:
            answer.add(n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,6]
        o = True
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [3,9,5]
        o = False
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [4,3,12,8]
        o = True
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_four(self):
        s = Solution()
        i = [4,3]
        o = False
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_five(self):
        s = Solution()
        i = [4,3,12,8,1]
        o = False
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_six(self):
        s = Solution()
        i = [11]
        o = True
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_seven(self):
        s = Solution()
        i = [11,11,11]
        o = True
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_eight(self):
        s = Solution()
        i = [1]
        o = True
        self.assertEqual(s.canTraverseAllPairs(i), o)

    def test_nine(self):
        s = Solution()
        i = [1,1]
        o = False
        self.assertEqual(s.canTraverseAllPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)