# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given an integer array nums and an integer k, return the k most
    frequent elements. Answer may be in any order.
    '''
    def topKFrequent_Counter(self, nums: List[int], k: int) -> List[int]:
        return [i for i,j in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        f = {}
        m = 0
        for n in nums:
            c[n] += 1
            m = max(m, c[n])
            if c[n] in f:
                f[c[n]].add(n)
            else:
                f[c[n]] = {n}
        a = set()
        for i in range(m, 0, -1):
            for j in f[i]:
                if j not in a:
                    a.add(j)
                    k -= 1
                    if k <= 0:
                        return list(a)
        return list(a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,2,2,3]
        j = 2
        o = [1,2]
        self.assertEqual(s.topKFrequent(i, j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        o = [1]
        self.assertEqual(s.topKFrequent(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)