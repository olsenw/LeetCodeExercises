# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of people people, which are the attributes of some
    people in a queue (not necessarily in order). Each
    people[i] = [hi, ki] represents the ith person of height hi with
    exactly ki other people in front who have a height greater than or
    equal to hi.

    Reconstruct and return the queue that is represented by the input
    array people. The returned queue should be formatted as an array
    queue, where queue[j] = [hj, kj] is the attributes of the jth
    person in the queue (queue[0] is the person at the front of the
    queue).
    '''
    # Help with logic from YJL1228
    # https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution
    # trick is to first sort by height (large -> small) then by k (small -> large)
    # then inserting them into list by their k value (which done in sequence
    # will be where that person needs to be inserted)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        o = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        self.assertEqual(s.reconstructQueue(i), o)

    def test_two(self):
        s = Solution()
        i = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
        o = [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
        self.assertEqual(s.reconstructQueue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)