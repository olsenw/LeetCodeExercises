# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n friends that are playing a game. The friends are sitting in a
    circle and are numbered from 1 to n in clockwise order. More formally,
    moving clockwise from the ith friend brings it to the (i+1)th friend for
    1 <= i < n, and moving clockwise from the nth friend brings it to the 1st
    friend.

    The rules of the game are as follows:
    1) Start at the 1st friend.
    2) Count the next k friends in clockwise direction including the friend
       starting at. The counting wraps around the circle and may count some
       friends more than once.
    3) The last friend counted leaves the circle and loses the game.
    4) If there is still more than one friend in the circle, go back to step 2
       starting from  the friend immediately clockwise of the friend who just
       lost and repeat.
    5) Else, the last friend in the circle wins the game.

    Given the number of friends, n, and an integer k, return the winner of the
    game.
    '''
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1,n+1))
        while len(queue) > 1:
            pass
            for _ in range(k % len(queue)):
                queue.append(queue.popleft())
            queue.pop()
        return queue[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5,2
        o = 3
        self.assertEqual(s.findTheWinner(*i), o)

    def test_two(self):
        s = Solution()
        i = 6,5
        o = 1
        self.assertEqual(s.findTheWinner(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)