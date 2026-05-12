# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array tasks where tasks[i] = [actuali, minimumi]:
    * actuali is the actual amount of energy needed to finish the ith task.
    * minimumi is the minimum amount of energy required to begin the ith task.

    The tasks can be completed in any order.

    Return the minimum initial amount of energy will need to finish all the
    tasks.
    '''
    # based on hints... which are almost the same as topic tags
    # binary search
    # trick is how to sort the tasks to complete
    # took a while looking at sample problem for pattern
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # tasks.sort(key=lambda x:(-x[1],x[0]))
        tasks.sort(key=lambda x:(-(x[1]-x[0]),-x[1],x[0]))
        def test(energy:int) -> bool:
            for a,m in tasks:
                if m > energy:
                    return False
                energy -= a
            return energy >= 0
        i = sum(t[0] for t in tasks)
        j = sum(t[1] for t in tasks)
        while i < j:
            # k = divmod(i+j, 2)
            # k = sum(k)
            k = (i+j) // 2
            if not test(k):
                i = k + 1
            else:
                j = k
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,4],[4,8]]
        o = 8
        self.assertEqual(s.minimumEffort(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[2,4],[10,11],[10,12],[8,9]]
        o = 32
        self.assertEqual(s.minimumEffort(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
        o = 27
        self.assertEqual(s.minimumEffort(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)