# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On a social network consisting of m users and some friendships between
    users, two users can communicate with each other if they know a common
    language.

    Given an integer n, an array languages, and an array friendships where:
    * There are n languages numbered 1 through n,
    * languages[i] is the set of languages the ith user knows, and
    * friendships[i] = [ui, vi] denotes a friendship between the users ui and
      vi.
    
    Choose one language and teach it to some users so that all friends can
    communicate with each other. Return the minimum number of users that need to
    be taught.

    Note that friendships are not transitive, meaning if x is a friend of y and
    y is a friend of z, this doesn't guarantee that x is a friend of z.
    '''
    # brute force
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        mismatch = []
        for i,j in friendships:
            if any(k in languages[j-1] for k in languages[i-1]):
                continue
            mismatch.append([i,j])
        answer = len(languages)
        for k in range(1,n+1):
            s = set()
            for i,j in mismatch:
                if k not in languages[i-1]:
                    s.add(i)
                if k not in languages[j-1]:
                    s.add(j)
            answer = min(answer, len(s))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [[1],[2],[1,2]]
        k = [[1,2],[1,3],[2,3]]
        o = 1
        self.assertEqual(s.minimumTeachings(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[2],[1,3],[1,2],[3]]
        k = [[1,4],[1,2],[3,4],[2,3]]
        o = 2
        self.assertEqual(s.minimumTeachings(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = [[1],[5],[1,5],[5]]
        k = [[1,2],[1,3],[1,4],[2,3]]
        o = 1
        self.assertEqual(s.minimumTeachings(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)