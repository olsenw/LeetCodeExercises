# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter
from math import factorial

class Solution:
    '''
    Given an integer array arr, and an integer target, return the number
    of tuples i, j, k such that i < j < k and
    arr[i] + arr[j] + arr[k] == target.

    Return answer modulo 10^9 + 7.
    '''
    # based on solution from leetcode
    # https://leetcode.com/problems/3sum-with-multiplicity/solution/
    # O(n^2) time
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        modulo = 1000000007
        arr.sort()
        ans = 0
        for i, a in enumerate(arr):
            t = target - arr[i]
            j = i + 1
            k = len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < t:
                    j += 1
                elif arr[j] + arr[k] > t:
                    k -= 1
                elif arr[j] != arr[k]:
                    l = r = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        l += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        r += 1
                        k -= 1
                    ans += l * r
                    ans %= modulo
                    j += 1
                    k -= 1
                else:
                    ans += (k - j + 1) * (k - j) // 2
                    ans %= modulo
                    break
        return ans

    # double counts some combinations
    # does not maintain index i < j < k correctly while case counting
    def threeSumMulti_FAILS(self, arr: List[int], target: int) -> int:
        # n! / k! (n-k)!
        def nck(n, k):
            return factorial(n) // (factorial(k) * factorial(n-k))
        def modulo(a, b):
            return ((a % 1000000007) + (b % 1000000007)) % 1000000007
        c = Counter(arr)
        t = 0
        keys = sorted(c.keys())
        for i, a in enumerate(keys):
            for j, b in enumerate(keys[i:], i):
                k = target - a - b
                if k in c:
                    if a == b == k and c[k] > 2:
                        t = modulo(nck(c[k], 3), t)
                    elif k == b and c[k] > 1:
                        t = modulo(nck(c[k], 2) * c[a], t)
                    if k > b:
                        if k == a and c[k] > 1:
                            t = modulo(nck(c[k], 2) * c[b], t)
                        elif a == b and c[a] > 1:
                            t = modulo(nck(c[a], 2) * c[k], t)
                        else:
                            t = modulo(c[a] * c[b] * c[k], t)
                            # t = ((c[a] * c[b] * c[k]) % modulo + t % modulo) % modulo
        return t

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,3,4,4,5,5]
        j = 8
        o = 20
        self.assertEqual(s.threeSumMulti(i, j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,2,2,2]
        j = 5
        o = 12
        self.assertEqual(s.threeSumMulti(i, j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        j = 3
        o = 1
        self.assertEqual(s.threeSumMulti(i, j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3]
        j = 3
        o = 0
        self.assertEqual(s.threeSumMulti(i, j), o)

    def test_fIVE(self):
        s = Solution()
        i = [1,2,0,3,2]
        j = 4
        o = 2
        self.assertEqual(s.threeSumMulti(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)