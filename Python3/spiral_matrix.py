# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a,b,c,d = 1, 0, len(matrix), len(matrix[0])
        i,j = 0,0
        answer = []
        while len(answer) < len(matrix) * len(matrix[0]):
            pass
            while j < d:
                answer.append(matrix[i][j])
                j += 1
            d -= 1
            i += 1
            j -= 1
            pass
            while i < c:
                answer.append(matrix[i][j])
                i += 1
            c -= 1
            i -= 1
            j -= 1
            pass
            while j >= b:
                answer.append(matrix[i][j])
                j -= 1
            b += 1
            i -= 1
            j += 1
            pass
            while i > a:
                answer.append(matrix[i][j])
                i -= 1
            a += 1
        pass
        return answer[:len(matrix) * len(matrix[0])]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(s.spiralOrder(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        o = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(s.spiralOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)