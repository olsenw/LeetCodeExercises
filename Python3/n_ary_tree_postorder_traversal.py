# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    '''
    Given the root of an n-ary tree, return the postorder traversal of its nodes
    values.

    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by
    the null value (See examples)
    '''
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        def dfs(node:'Node'):
            if node is None:
                return
            for c in node.children:
                dfs(c)
            answer.append(node.val)
        dfs(root)
        return answer

class UnitTesting(unittest.TestCase):
    '''tested on Leetcode'''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)