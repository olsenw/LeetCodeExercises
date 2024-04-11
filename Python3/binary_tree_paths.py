# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, return all root-to-leaf paths in any order.

    A leaf is a node with no children.
    '''
    def binaryTreePaths_wrong(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        temp = []
        def dfs(node: Optional[TreeNode]):
            nonlocal temp
            nonlocal answer
            if node is None:
                if len(temp) > 0:
                    answer.append("->".join(str(t) for t in temp))
                return
            temp.append(node.val)
            dfs(node.left)
            dfs(node.right)
            temp.pop()
            return
        dfs(root)
        return answer

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        temp = []
        def dfs(node: TreeNode):
            temp.append(str(node.val))
            if node.left is None and node.right is None:
                answer.append("->".join(temp))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            temp.pop()
            return
        if root is not None:
            dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)