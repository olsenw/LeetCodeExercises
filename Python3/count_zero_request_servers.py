# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n denoting the total number of servers and a 2D 0-indexed
    integer array logs, where logs[i] = [server_id, time] denotes that the
    server id server_id received a request at time time.

    Also given an integer x and a 0-indexed integer array queries.

    Return a 0-indexed integer array arr of length queries.length where arr[i]
    represents the number of servers that did not receive any requests during
    the time interval [queries[i] - x, queries[i]].

    Note that the time intervals are inclusive.
    '''
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(logs)
        c = Counter()
        answer = [0] * len(queries)
        logs.sort(key=lambda x:(x[1],x[0]))
        squeries = sorted((range(len(queries))), key= lambda i: queries[i]-x)
        served = 0
        i = 0
        while i < m and logs[i][1] < queries[squeries[0]] - x:
            i += 1
        j = i
        for q in squeries:
            left,right = queries[q]-x,queries[q]
            while i < m and logs[i][1] < left:
                c[logs[i][0]] -= 1
                if c[logs[i][0]] == 0:
                    served -= 1
                i += 1
            while j < m and logs[j][1] <= right:
                c[logs[j][0]] += 1
                if c[logs[j][0]] == 1:
                    served += 1
                j += 1
            answer[q] = n - served
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,3],[2,6],[1,5]]
        k = 5
        l = [10,11]
        o = [1,2]
        self.assertEqual(s.countServers(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[2,4],[2,1],[1,2],[3,1]]
        k = 2
        l = [3,4]
        o = [0,1]
        self.assertEqual(s.countServers(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)