# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a school that has classes of students and each class will be having
    a final exam. Given a 2D integer array classes, where
    classes[i] = [passi, totali]. It is known beforehand that in the ith class
    there are totali total students, but only passi number of students will pass
    the exam.

    Also given an integer extraStudents. There are another extraStudents
    brilliant students that are guaranteed to pass the exam of any class they
    are assigned to. Assign each of the extraStudents students to a class in a
    way that maximizes the average pass ratio across all the classes.

    The pass ratio of a class is equal to the number of students of the class
    that will pass the exam divided by the total number of students of the
    class. The average pass ratio is the sum of pass ratios of all the classes
    divided by the number of the classes.

    Return the maximum possible average pass ratio after assigning the
    extraStudents students. Answers withing 10^-5 of the actual answer will be
    accepted.
    '''
    def maxAverageRatio_fails(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(i / j, j, i) for i,j in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            i,j,k = heapq.heappop(heap)
            heapq.heappush(heap, ((k+1)/(j+1),j+1,k+1))
        return sum(i for i,_,_ in heap) / len(heap)

    def maxAverageRatio_fails2(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(j,i) for i,j in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            j,i = heap[0]
            heapq.heapreplace(heap, (j+1,i+1))
        return sum(i/j for i,j in heap) / len(heap)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(-(((i+1)/(j+1)) - (i/j)),i,j) for i,j in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            _,i,j = heap[0]
            i += 1
            j += 1
            heapq.heapreplace(heap, (-(((i+1)/(j+1)) - (i/j)),i,j))
        return sum(i / j for _,i,j in heap) / len(heap)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,5],[2,2]]
        j = 2
        o = 0.78333
        self.assertAlmostEqual(s.maxAverageRatio(i,j), o, 5)

    def test_two(self):
        s = Solution()
        i = [[2,4],[3,9],[4,5],[2,10]]
        j = 4
        o = 0.53485
        self.assertAlmostEqual(s.maxAverageRatio(i,j), o, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)