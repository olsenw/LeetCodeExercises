# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given the logs for users; actions on LeetCode, and an integer k. The logs
    are represented by a 2D integer array logs where each logs[i] = [IDi, timei]
    indicates that the user with IDi performed an action at the minute timei.

    Multiple users can perform actions simultaneously, and a single user can
    perform multiple actions in the same minute.

    The user active minutes (UAM) for a given user is defined as the number of
    unique minutes in which the user performed an action on LeetCode. A minute
    can only be counted once; even if multiple actions occur during it.

    Calculate a 1-indexed array answer of size k such that, for each j
    (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

    Return the array answer as described above.
    '''
    def findingUsersActiveMinutes_slow(self, logs: List[List[int]], k: int) -> List[int]:
        uam = Counter()
        logSet = set()
        for id, minute in logs:
            if (id, minute) not in logSet:
                logSet.add((id, minute))
                uam[id] += 1
        answer = Counter()
        for user in uam:
            answer[uam[user]] += 1
        return [answer[i] for i in range(1, k+1)]

    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        logs.sort()
        logs.append([[float('inf'), float('inf')]])
        id = logs[0][0]
        minutes = 1
        for i in range(1, len(logs)):
            if logs[i-1] == logs[i]:
                continue
            if id == logs[i][0]:
                minutes += 1
            else:
                answer[minutes-1] += 1
                id = logs[i][0]
                minutes = 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,5],[1,2],[0,2],[0,5],[1,3]]
        j = 5
        o = [0,2,0,0,0]
        self.assertEqual(s.findingUsersActiveMinutes(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[2,3]]
        j = 4
        o = [1,1,0,0]
        self.assertEqual(s.findingUsersActiveMinutes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)