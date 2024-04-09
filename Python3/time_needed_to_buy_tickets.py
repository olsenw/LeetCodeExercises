# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n people in a line queuing to buy tickets, where the 0th person is
    at the front of the line and (n - 1)th person is at the back of the line.

    Given a 0-indexed integer array tickets of length n where the number of
    tickets that the ith person would like to buy is tickets[i].

    Each person takes exactly 1 second to buy a ticket. A person can only buy 1
    ticket at a time and has to go back to the end of the line (which happens
    instantaneously) in order to buy more tickets. If a person does not have any
    tickets left to buy, the person will leave the line.

    Return the time taken for the person at position k (0-indexed) to finish
    buying tickets.
    '''
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        tickets = deque(enumerate(tickets))
        while tickets:
            i,j = tickets.popleft()
            answer += 1
            if i == k and j == 1:
                return answer
            if j > 1:
                tickets.append((i,j-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,2]
        j = 2
        o = 6
        self.assertEqual(s.timeRequiredToBuy(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,1,1,1]
        j = 0
        o = 8
        self.assertEqual(s.timeRequiredToBuy(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)