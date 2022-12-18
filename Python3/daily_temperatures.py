# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers temperatures representing the daily temperatures,
    return an array answer such that answer[i] is the number of days after the
    ith day that a warmer temperature occurs. If there is no future day for
    which this is possible keep answer[i] == 0 instead.'''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        monotonic = [(temperatures[-1],0)]
        for i in range(n - 2, -1, -1):
            days = 1
            while monotonic and monotonic[-1][0] <= temperatures[i]:
                days += 1 + monotonic.pop()[1]
            answer[i] = days if monotonic else 0
            monotonic.append((temperatures[i],days-1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [73,74,75,71,69,72,76,73]
        o = [1,1,4,2,1,1,0,0]
        self.assertEqual(s.dailyTemperatures(i), o)

    def test_two(self):
        s = Solution()
        i = [30,40,50,60]
        o = [1,1,1,0]
        self.assertEqual(s.dailyTemperatures(i), o)

    def test_three(self):
        s = Solution()
        i = [30,60,90]
        o = [1,1,0]
        self.assertEqual(s.dailyTemperatures(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)