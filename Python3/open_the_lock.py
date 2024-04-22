# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from itertools import product
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a lock with four circular wheels. Each wheel has 10 slots: '0',
    '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely
    and wrap around. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the
    four wheels.

    Given a list of deadends dead ends, meaning if the lock displays any of
    these codes, the wheels of the lock will stop turning and will no longer
    open.

    Given a target representing the value of the wheels that will unlock the
    lock, return the minimum total number of turns required to open the lock, or
    -1 if it is impossible.
    '''
    def openLock_time_limit_exceeded(self, deadends: List[str], target: str) -> int:
        graph = {''.join(i):[] for i in product('0123456789', repeat=4)}
        for i in graph:
            for j in range(len(i)):
                k = int(i[j])
                graph[i].append(f'{i[:j]}{(k-1) % 10}{i[j+1:]}')
                graph[i].append(f'{i[:j]}{(k+1) % 10}{i[j+1:]}')
        visited = set(deadends)
        def dfs(node):
            if node == target:
                return 0
            visited.add(node)
            answer = 10000
            for i in graph[node]:
                if i not in visited:
                    answer = min(answer, 1 + dfs(i))
            visited.remove(node)
            return answer
        a = dfs('0000')
        return -1 if a >= 10000 else a

    def openLock(self, deadends: List[str], target: str) -> int:
        graph = {''.join(i):[] for i in product('0123456789', repeat=4)}
        for i in graph:
            for j in range(len(i)):
                k = int(i[j])
                graph[i].append(f'{i[:j]}{(k-1) % 10}{i[j+1:]}')
                graph[i].append(f'{i[:j]}{(k+1) % 10}{i[j+1:]}')
        visited = set(deadends)
        q = deque([('0000',0)])
        while q:
            n,d = q.popleft()
            if n in visited:
                continue
            if n == target:
                return d
            visited.add(n)
            q.extend((g, d+1) for g in graph[n])
        return -1
    
    '''
    Could probably improve by generating the graph as needed instead of before.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["0201","0101","0102","1212","2002"]
        j = "0202"
        o = 6
        self.assertEqual(s.openLock(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["8888"]
        j = "0009"
        o = 1
        self.assertEqual(s.openLock(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["8888"]
        j = "0009"
        o = 1
        self.assertEqual(s.openLock(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)