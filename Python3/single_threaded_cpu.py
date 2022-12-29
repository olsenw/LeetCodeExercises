# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n tasks labeled from 0 to n - 1 represented by a 2D integer array
    tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith
    task will be available to process at enqueueTimei and will take
    processingTimei to finish processing.

    There is a single-threaded CPU that can process at most one task at a time
    and will act in the following way:
    * If the CPU is idle and there are no available tasks to process, the CPU
      remains idle.
    * If the CPU is idle and there are available tasks, the CPU will choose the
      one with the shortest processing time. If multiple tasks have the same
      shortest processing time, it will choose the task with the smallest index.
    * Once a task is started, the CPU will process the entire task without
      stopping.
    * The CPU can finish a task then start a new one instantly.

    Return the order in which the CPU will process the tasks.
    '''
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        answer = []
        available = deque(sorted(range(len(tasks)), key=lambda x: tasks[x]))
        heap = []
        time = tasks[available[0]][0]
        while available or heap:
            while available and tasks[available[0]][0] <= time:
                heapq.heappush(heap, (tasks[available[0]][1], available.popleft()))
            if not heap:
                time = tasks[available[0]][0]
                continue
            process, index = heapq.heappop(heap)
            time += process
            answer.append(index)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,4],[3,2],[4,1]]
        o = [0,2,3,1]
        self.assertEqual(s.getOrder(i), o)

    def test_two(self):
        s = Solution()
        i = [[7,10],[7,12],[7,5],[7,4],[7,2]]
        o = [4,3,2,0,1]
        self.assertEqual(s.getOrder(i), o)

    def test_three(self):
        s = Solution()
        i = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
        o = [4,3,2,0,1]
        self.assertEqual(s.getOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)