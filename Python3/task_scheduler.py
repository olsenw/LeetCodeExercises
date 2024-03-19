# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of CPU tasks, each represented by letters A to Z, and a
    cooling time, n. each cycle or interval allows the completion of one task.
    Tasks can be completed in any order, but there's a constraint: identical
    tasks must be separated by at least n intervals due to cooling time.

    Return the minimum number of intervals required to complete all tasks.
    '''
    # wrong, counting something incorrectly
    def leastInterval_wrong(self, tasks: List[str], n: int) -> int:
        answer = 0
        c = Counter(tasks)
        h = [(c[i], i) for i in c]
        heapq.heapify(h)
        while h:
            l = []
            for _ in range(n+1):
                if h:
                    x,y = heapq.heappop(h)
                    l.append((x-1,y))
            # answer += max(n+1,len(l))
            a = 0
            for i in l:
                if i[0]:
                    heapq.heappush(h,i)
                a += 1
            if h:
                answer += n
            else:
                answer += a
        return answer

    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = [-c[i] for i in c]
        heapq.heapify(h)
        w = deque()
        a = 0
        while h or w:
            # if h and h[0] > 1:
                # w.append((a + n, heapq.heappop(h) - 1))
            if h:
                x = heapq.heappop(h) + 1
                if -x:
                    w.append((a+n, x))
            a += 1
            if w and a > w[0][0]:
                heapq.heappush(h, w.popleft()[1])
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["A","A","A","B","B","B"]
        j = 2
        o = 8
        self.assertEqual(s.leastInterval(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["A","C","A","B","D","B"]
        j = 1
        o = 6
        self.assertEqual(s.leastInterval(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["A","A","A", "B","B","B"]
        j = 3
        o = 10
        self.assertEqual(s.leastInterval(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["A","B","A"]
        j = 2
        o = 4
        self.assertEqual(s.leastInterval(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)