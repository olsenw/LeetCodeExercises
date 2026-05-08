# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python
# Sieve of Eratosthenes implementation
def primeGenerator():
    d: Dict[int, List[int]] = dict()
    q = 2
    while True:
        if q not in d:
            yield q
            d[q*q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p+q, []).append(p)
            del d[q]
        q += 1
primes = []
for p in primeGenerator():
    if p > 10**6:
        break
    primes.append(p)

# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
# brute force way to get prime factors
@cache
def primeFactors(n:int) -> Set[int]:
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

class Solution:
    '''
    Given an integer array nums of length n.

    Starting at index 0, reach the index n-1.

    From any index i, one of the following operations may be preformed:
    * Adjacent Step: Jump to index i+1 or i-1, if the index is within bounds.
    * Prime Teleportation: If nums[i] is a prime number p, it is possible to
      instantly jump to any index j != i such that nums[j] % p == 0.

    Return the minimum number of jumps required to reach index n-1.
    '''
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(list)
        for i,j in enumerate(nums):
            for p in primeFactors(j):
                d[p].append(i)
        # (jumps, index)
        h = [(0,0)]
        v = set()
        while h:
            jumps,index = heapq.heappop(h)
            if index == n-1:
                return jumps
            if index in v:
                continue
            v.add(index)
            if index > 0 and index - 1 not in v:
                heapq.heappush(h, (jumps+1,index-1))
            if index < n-1 and index + 1 not in v:
                heapq.heappush(h, (jumps+1,index+1))
            if nums[index] in d:
                for i in d[nums[index]]:
                    if i not in v:
                        heapq.heappush(h, (jumps+1,i))
                # based on hint 3
                # only need to visit each one once
                d[nums[index]].clear()
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4,6]
        o = 2
        self.assertEqual(s.minJumps(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,7,9]
        o = 2
        self.assertEqual(s.minJumps(i), o)

    def test_three(self):
        s = Solution()
        i = [4,6,5,8]
        o = 3
        self.assertEqual(s.minJumps(i), o)

    def test_four(self):
        s = Solution()
        i = [5] * (10**5)
        o = 1
        self.assertEqual(s.minJumps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)