# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Given the root of a binary tree, return the average value of the
    nodes on each level in the form of an array. Answers within 10^-5 of
    the actual answer will be accepted.
    '''
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        average = [root]
        while average:
            answer.append(sum(a.val for a in average) / len(average))
            update = []
            for a in average:
                if a.left:
                    update.append(a.left)
                if a.right:
                    update.append(a.right)
            average = update
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        o = [3.0,14.5,11.0]
        self.assertEqual(s.averageOfLevels(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
        o = [3.0,14.5,11.0]
        self.assertEqual(s.averageOfLevels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)