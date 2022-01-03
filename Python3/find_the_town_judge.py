# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    In a town there are n people labeled from 1 to n. There is a rumor
    that one of these people is secretly the town judge.

    If the town judge exists, then:
    1. The town judge trusts nobody
    2. Everybody [not the town judge] trusts the town judge
    3. There is exactly one person that satisfies properties 1 and 2.

    Given an array trust where trust[i] = [ai,bi] representing that 
    person labeled ai trusts the person labeled bi.

    Return the label of the town judge if the town judge exists and can
    be identified, or return -1 otherwise.
    '''
    # O(n) time (counter slows down here... not done in C apparently)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            if n > 1:
                return -1
            return 1
        notrust = {i for i in range(1, n+1)}
        from collections import Counter
        count = Counter()
        for a,b in trust:
            notrust.discard(a)
            count[b] += 1
        if len(notrust) == 1:
            j = notrust.pop()
            if j == count.most_common(1)[0][0]:
                return j
        return -1

    # O(n) faster because python really like dictionaries
    def findJudge_dict(self, n: int, trust: List[List[int]]) -> int:
        if not len(trust): return 1 if n < 2 else -1
        s = set()
        d = dict()
        for a,b in trust:
            s.add(a)
            if b not in d:
                d[b] = 1
            else:
                d[b] += 1
        for k in d:
            if d[k] == n-1 and k not in s:
                return k
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        n = 2
        i = [[1,2]]
        o = 2
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_two(self):
        s = Solution()
        n = 3
        i = [[1,3],[2,3]]
        o = 3
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_three(self):
        s = Solution()
        n = 3
        i = [[1,3],[2,3],[3,1]]
        o = -1
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_four(self):
        s = Solution()
        n = 1
        i = []
        o = 1
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_five(self):
        s = Solution()
        n = 2
        i = []
        o = -1
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_six(self):
        s = Solution()
        n = 4
        i = [[1,3],[1,4],[2,3]]
        o = -1
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

    def test_seven(self):
        s = Solution()
        n = 3
        i = [[1,2],[2,3]]
        o = -1
        self.assertEqual(s.findJudge(n, i), o)
        self.assertEqual(s.findJudge_dict(n, i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)