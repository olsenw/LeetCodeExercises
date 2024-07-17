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
    Given the root of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in to_delete, a forest (disjoint union
    of trees) remains.

    Return the root of the trees in the remaining forest. The result may be
    returned in any order.
    '''
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        answer = []
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None
            if node.val in to_delete:
                if node.left:
                    answer.append(node.left)
                if node.right:
                    answer.append(node.right)
                return True
            return False
        dfs(root)
        if root.val not in to_delete:
            answer.append(root)
        return answer

class UnitTesting(unittest.TestCase):
    pass
    '''
    Tested online using leetcode
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)