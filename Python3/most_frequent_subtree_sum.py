# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        c = Counter()
        def dfs(node:Optional[TreeNode]):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left + right + node.val
            c[s] += 1
            return s
        dfs(root)
        answer = []
        for i,j in c.most_common():
            if answer and c[answer[0]] != j:
                break
            answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(5, TreeNode(2), TreeNode(-3))
        o = [2,-3,4]
        self.assertEqual(s.findFrequentTreeSum(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(5, TreeNode(2), TreeNode(-5))
        o = [2]
        self.assertEqual(s.findFrequentTreeSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)