# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    def __eq__(self, o) -> bool:
        return self.val == o.val \
            and self.isLeaf == o.isLeaf \
            and self.topLeft == o.topLeft \
            and self.topRight == o.topRight \
            and self.bottomLeft == o.bottomLeft\
            and self.bottomRight == o.bottomRight

class Solution:
    '''
    Given a n x n matrix grid of 0's and 1's only. Represent the grid with a
    Quad-Tree.

    Return the root of the Quad-Tree representing the grid.

    Notice that it is possible to assign the value of a node to True or False
    when isLeaf is False, and both will be accepted in the answer.

    A Quad-Tree is a tree data structure in which each internal node has exactly
    four children. Besides each node two attributes:
    * val: True if the node represents a grid of 1's or False if the node
      represents a grid of 0's.
    * isLeaf: True if the node is a leaf node on the tree or False if the node
      has four children.
    
    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;
    }

    A Quad-tree can be constructed from a two-dimensional area using the
    following steps:

    If the current grid has the same value (ie all 1's or all 0') set isLeaf
    True and set val to value of the grid and set the four children to Null and
    stop.

    If the current grid has different values, set isLeaf to False and set val to
    any value and divide the current grid into four sub-grids as shown in the
    photo.

    Recurse for each of the children with the proper sub-grid.
    '''
    def construct(self, grid: List[List[int]]) -> Node:
        def divide(a:int,b:int,c:int,d:int) -> Node:
            # base case single cell
            if a == b and c == d:
                return Node(grid[a][c], True, None, None, None, None)
            mx = (b - a) // 2 + a
            my = (d - c) // 2 + c
            tl = divide(a, mx, c, my)
            bl = divide(mx+1, b, c, my)
            tr = divide(a, mx, my+1, d)
            br = divide(mx+1, b, my+1, d)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf \
                and tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True,  None, None, None, None)
            return Node(3, False, tl, tr, bl, br)
        return divide(0, len(grid) - 1, 0, len(grid) - 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,0]]
        o = Node(3,False,
                Node(0,True,None,None,None,None),
                Node(1,True,None,None,None,None),
                Node(1,True,None,None,None,None),
                Node(0,True,None,None,None,None),
            )
        self.assertEqual(s.construct(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1]]
        o = Node(3,False,
                Node(0,True,None,None,None,None),
                Node(0,True,None,None,None,None),
                Node(1,True,None,None,None,None),
                Node(1,True,None,None,None,None),
            )
        self.assertEqual(s.construct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)