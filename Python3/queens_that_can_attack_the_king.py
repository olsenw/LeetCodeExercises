# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one
    white king.

    Given a 2D integer array queens where queens[i] = [xQueeni, yQueeni]
    represents the position of the ith black queen on the chessboard. Also given
    an integer array king of length 2 where king = [xKing, yKing] represents the
    position of the white king.

    Return the coordinates of the black queens that can directly attack the
    king. The answer may be returned in any order.
    '''
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        a,b = king
        board = [[0] * 8 for _ in range(8)]
        board[a][b] = 2
        for x,y in queens:
            board[x][y] = 1
        def direction(values):
            for a,b in values:
                if board[a][b]:
                    return board[a][b] == 2
            return False
        def test(x,y):
            return any([
                # N
                direction(zip(range(x-1,-1,-1), [y]*8)),
                # NE
                direction(zip(range(x-1,-1,-1), range(y+1,8))),
                # E
                direction(zip([x]*8, range(y+1,8))),
                # SE
                direction(zip(range(x+1,8), range(y+1,8))),
                # S
                direction(zip([x]*8, range(y-1,-1,-1))),
                # SW
                direction(zip(range(x+1,8), range(y-1,-1,-1))),
                # W
                direction(zip(range(x+1,8), [y]*8)),
                # NW
                direction(zip(range(x-1,-1,-1), range(y-1,-1,-1))),
            ])
        return [i for i in queens if test(*i)]
        # answer = []
        # for x,y in queens:
        #     if test(x,y):
        #         answer.append([x,y])
        # return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
        j = [0,0]
        o = [[0,1],[1,0],[3,3]]
        self.assertEqual(s.queensAttacktheKing(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
        j = [3,3]
        o = [[2,2],[3,4],[4,4]]
        self.assertEqual(s.queensAttacktheKing(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)