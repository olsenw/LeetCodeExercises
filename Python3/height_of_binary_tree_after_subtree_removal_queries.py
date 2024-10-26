# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree with n nodes. Each node is assigned a unique
    value from 1 to n. Also given is an array queries of size m.

    Perform m independent queries on the the tree where in the ith query the
    following steps are performed:
    * Remove the subtree rooted at the node with the value queries[i] from the
      tree. It is guaranteed that queries[i] will not be qual to the value of
      the root.
    
    Return an array answer of size m where answer[i] is the height of the tree
    after performing the ith query.

    Note:
    * The queries are independent, so the tree returns to its initial state
      after each query.
    * The height of a tree is the number of edges in the longest simple path
      from the root to some node in the tree.
    '''
    def treeQueries_fails(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = dict()
        rows = dict()
        def dfs(node: TreeNode, depth: int):
            heights[node.val] = [depth,depth]
            if depth in rows:
                rows[depth].append(node.val)
            else:
                rows[depth] = [node.val]
            if node.left:
                heights[node.val][1] = max(heights[node.val][1], dfs(node.left, depth+1))
            if node.right:
                heights[node.val][1] = max(heights[node.val][1], dfs(node.right, depth+1))
            return heights[node.val][1]
        depth = dfs(root, 0)
        answer = []
        for q in queries:
            m = 0
            for r in rows[heights[q][0]]:
                if r != q:
                  m = max(m, heights[r][1])
            answer.append(m)
        return answer
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = dict()
        rows = dict()
        def dfs(node: TreeNode, depth: int):
            heights[node.val] = [depth,depth]
            if depth in rows:
                rows[depth].append(node.val)
            else:
                rows[depth] = [node.val]
            if node.left:
                heights[node.val][1] = max(heights[node.val][1], dfs(node.left, depth+1))
            if node.right:
                heights[node.val][1] = max(heights[node.val][1], dfs(node.right, depth+1))
            return heights[node.val][1]
        depth = dfs(root, 0)
        calcs = [[[0,0]]]
        for d in range(1, depth+1):
            l = [[heights[r][1],r] for r in rows[d]]
            # l.append(calcs[d-1][0])
            l.append([d-1,0])
            calcs.append(sorted(l, reverse=True))
            # calcs.append(sorted([[heights[r],r] for r in rows[d]] + [calcs[d-1][0]], reverse=True))
        answer = []
        for q in queries:
            depth = heights[q][0]
            a = calcs[depth][0]
            b = calcs[depth][1]
            answer.append(a[0] if a[1] != q else b[0])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(3, TreeNode(2)), TreeNode(4, TreeNode(6), TreeNode(5, None, TreeNode(7))))
        j = [4]
        o = [2]
        self.assertEqual(s.treeQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
        j = [3,2,4,8]
        o = [3,2,3,2]
        self.assertEqual(s.treeQueries(i,j), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        j = [2,3,4]
        o = [0,1,2]
        self.assertEqual(s.treeQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)