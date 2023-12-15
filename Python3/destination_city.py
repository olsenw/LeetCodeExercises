# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array paths, where paths[i] = [cityAi, cityBi] means there exists
    a direct path going from cityAi to cityBi. Return the destination city, that
    is, the city without any path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop,
    therefore, there will be exactly one destination city.
    '''
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set(i for i,_ in paths)
        for _,i in paths:
            if i not in starts:
                return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        o = "Sao Paulo"
        self.assertEqual(s.destCity(i), o)

    def test_two(self):
        s = Solution()
        i = [["B","C"],["D","B"],["C","A"]]
        o = "A"
        self.assertEqual(s.destCity(i), o)

    def test_two(self):
        s = Solution()
        i = [["A","Z"]]
        o = "Z"
        self.assertEqual(s.destCity(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)