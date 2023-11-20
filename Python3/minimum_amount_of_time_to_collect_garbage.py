# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of strings garbage where garbage[i] represents the
    assortment of garbage at the ith house. gabage[i] consists only of the
    characters 'M', 'P' and 'G' representing one unit of metal, paper and glass
    garbage respectively. Picking up one unit of any type of garbage takes 1
    minute.

    Given 0-indexed integer array travel where travel[i] is the number of
    minutes needed to go from house i to house i + 1.

    There are three garbage trucks in the city, each responsible for picking up
    one type of garbage. Each garbage truck starts at house 0 and must visit
    each house in order; however, they do not need to visit every house.

    Only one garbage truck may be used at any given moment. While one truck is
    driving or picking up garbage, the other two trucks cannot do anything.

    Return the minimum number of minutes needed to pick up all the garbage.
    '''
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.append(0)
        answer = 0
        a,b,c = 0,0,0
        for s,t in zip(garbage,travel):
            x = s.count('M')
            y = s.count('P')
            z = s.count('G')
            if x:
                answer += a + x
                a = 0
            if y:
                answer += b + y
                b = 0
            if z:
                answer += c + z
                c = 0
            a += t
            b += t
            c += t
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["G","P","GP","GG"]
        j = [2,4,3]
        o = 21
        self.assertEqual(s.garbageCollection(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["MMM","PGM","GP"]
        j = [3,10]
        o = 37
        self.assertEqual(s.garbageCollection(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)