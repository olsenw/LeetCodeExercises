# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given n tasks and m workers. Each task has a strength requirement store in a
    0-indexed integer array tasks, with the ith task requiring tasks[i] strength
    to complete. The strength of each worker is stored in a 0-indexed integer
    array workers, with the jth worker having workers[j] strength. Each worker
    can only be assigned to a single task and must have a strength greater than
    or equal to the task's strength requirement (ie workers[j] >= tasks[i]).

    Additionally, there are pills magical pills that will increase a workers
    strength by strength. It is possible to decide which workers receive the
    magical pills, however, each worker can receive at most one magical pill.

    Given the 0-indexed integer arrays task and workers and the integers pills
    and strength, return the maximum number of tasks that can be completed.
    '''
    def maxTaskAssign_fails(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        answer = 0
        m,n = len(workers), len(tasks)
        workers.sort()
        tasks.sort()
        j = 0
        for i in range(n):
            if workers[j] >= tasks[i]:
                answer += 1
            elif pills and workers[j] + strength >= tasks[i]:
                answer += 1
                pills -= 1
            j += 1
            if j == m:
                break
        return answer

    def maxTaskAssign_fails(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        mono = []
        pill = []
        tasks.sort()
        workers.sort()
        for t in tasks:
            i = bisect.bisect_left(workers, t)
            j = bisect.bisect_left(workers, t - strength)
            mono.append(len(workers) - i)
            pill.append(len(workers) - j)
        pass
        def _test(k:int) -> bool:
            q = []
            j = 0
            p = 0 # how many pills popped from the worker queue
            for i in range(len(tasks)):
                if workers[j] >= tasks[i]:
                    answer += 1
                    j += 1
                    continue
                while j < len(workers) and workers[j] < tasks[i]:
                    if p < pills and q and q[0] >= tasks[i]:
                        p += 1
                        heapq.heappop(q)
                        answer += 1
                        break
                    else:
                        heapq.heappush(q, workers[j] + strength)
                    j += 1
            return False
        i,j = 0, len(tasks)-1
        while i < j:
            k = i + (j - i) // 2
            t = min(pill[k] - mono[k], pills) + mono[k]
            if t >= k:
                i = k + 1
            else:
                j = k - 1
        return i

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/editorial/?envType=daily-question&envId=2025-05-01
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n,m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        def check(k:int) -> bool:
            p = pills
            # ordered list of k strongest workers
            ws = SortedList(workers[m-k:])
            # enumerate each task from small to large
            for i in range(k-1, -1, -1):
                # largest element in ordered set is better than task
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    j = ws.bisect_left(tasks[i] - strength)
                    if j == len(ws):
                        return False
                    p -= 1
                    ws.pop(j)
            return True
        i,j = 1, min(n,m)
        answer = 0
        while i <= j:
            k = i + (j-i) // 2
            if check(k):
                answer = k
                i = k + 1
            else:
                j = k - 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,1]
        j = [0,3,3]
        k = 1
        l = 1
        o = 3
        self.assertEqual(s.maxTaskAssign(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = [5,4]
        j = [0,0,0]
        k = 1
        l = 5
        o = 1
        self.assertEqual(s.maxTaskAssign(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = [10,15,30]
        j = [0,10,10,10,10]
        k = 3
        l = 10
        o = 2
        self.assertEqual(s.maxTaskAssign(i,j,k,l), o)

    def test_four(self):
        s = Solution()
        i = [5,9,8,5,9]
        j = [1,6,4,2,6]
        k = 1
        l = 5
        o = 3
        self.assertEqual(s.maxTaskAssign(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)