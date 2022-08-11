# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def r(node, small, large):
            if not node:
                return True
            if not (small < node.val < large):
                return False
            if not r(node.left, small, node.val):
                return False
            if not r(node.right, node.val, large):
                return False
            return True
        return r(root, float('-inf'), float('inf'))

class UnitTesting(unittest.TestCase):
    '''
    Did it on phone and it passed
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)