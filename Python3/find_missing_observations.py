# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n + m observations of 6-sided dice rolls with each face numbered
    from 1 to 6. n of the observations went missing, and there are now only m
    observations. Fortunately, the average value of the n + m rolls.

    Given an integer array rolls of length m where rolls[i] is the value of the
    ith observation. Also given are two integers mean and n.

    Return an array of length n containing the missing observations such that
    the average value of the n + m rolls is exactly mean. If there are multiple
    valid answers, return any of them. If no such array exists return an empty
    array.

    The average value of a set of k numbers is the sum of the numbers divided by
    k.

    Note that mean is an integer, so the sum of the n + m rolls should be
    divisible by n + m.
    '''
    # the hint helped a lot
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = sum(rolls)
        t = mean * (n + len(rolls)) - s
        if not (n <= t <= 6 * n):
            return []
        t -= n
        answer = [1] * n
        for i in range(n):
            if t < 5:
                answer[i] += t
                break
            answer[i] += 5
            t -= 5
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,4,3]
        j = 4
        k = 2
        self.assertEqual(s.missingRolls(i,j,k), [6,6])

    def test_two(self):
        s = Solution()
        i = [1,5,6]
        j = 3
        k = 4
        self.assertEqual(s.missingRolls(i,j,k), [6,1,1,1])

    def test_three(self):
        s = Solution()
        i = [1,2,3,4]
        j = 6
        k = 4
        self.assertEqual(s.missingRolls(i,j,k), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)