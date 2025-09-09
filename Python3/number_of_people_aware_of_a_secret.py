# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On day 1, one person discovers a secret.

    Given an integer delay, which means that each person will share the secret
    with a new person every day, starting from delay days after discovering the
    secret. Also given an integer forget, which means that each person will
    forget, which means that each person will forget the secret forget days
    after discovering it. A person cannot share the secret on the same day they
    forgot it, or on any day afterwards.

    Given an integer n, return the number of people who know the secret at the
    end of day n. Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    # simulation
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        m = 10**9 + 7
        gone = deque([(1+forget,1)])
        wait = deque([(1+delay,1)])
        spreading = 0
        for i in range(1,n+1):
            while gone and gone[0][0] == i:
                a,b = gone.popleft()
                spreading -= b
            while wait and wait[0][0] == i:
                a,b = wait.popleft()
                spreading += b
            if spreading:
                wait.append((i + delay, spreading))
                gone.append((i + forget, spreading))
        answer = spreading + sum(b for a,b in wait)
        return answer % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6,2,4
        o = 5
        self.assertEqual(s.peopleAwareOfSecret(*i), o)

    def test_two(self):
        s = Solution()
        i = 4,1,3
        o = 6
        self.assertEqual(s.peopleAwareOfSecret(*i), o)

    def test_three(self):
        s = Solution()
        i = 1000,2,4
        o = 439994839
        self.assertEqual(s.peopleAwareOfSecret(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)