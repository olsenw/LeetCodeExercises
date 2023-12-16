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
    Given the root of a binary tree and an integer targetSum, return the number
    of paths where the sum of the values along the path equals targetSum.

    The path does not need to start or end at the root or a leaf, but it must go
    downwards (ie, traveling only from parent nodes to child nodes).
    '''
    def pathSum_wrong(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], value: int):
            answer = 0
            if value == targetSum:
                answer += 1
            if not node:
                return answer
            answer += dfs(node.left, value + node.val)
            answer += dfs(node.right, value + node.val)
            return answer
        if not root:
            return 0
        answer = 0
        answer += self.pathSum(root.left, targetSum)
        answer += self.pathSum(root.right, targetSum)
        return answer + dfs(root,0)

    # O(N^2)
    # based on editorial
    # had simlar idea in wrong
    def pathSum_brute(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = 0
        def check(node: Optional[TreeNode], target: int):
            nonlocal answer
            if node is None:
                return
            if node.val == target:
                answer += 1
            check(node.left, target - node.val)
            check(node.right, target - node.val)
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            check(node, targetSum)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return answer

    # O(n) time and space
    # also based on editorial
    def pathSum_memorization(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = 0
        # maps the frequency of sums during dfs
        cache = {0:1}
        def dfs(node: Optional[TreeNode], current):
            nonlocal answer
            if node is None:
                return
            # update current path sum
            current += node.val
            # is there a valid path sum in past (current - old == target)
            old = current - targetSum
            # if valid ending node update the answer
            answer += cache.get(old, 0)
            # cache current path sum frequency
            cache[current] = cache.get(current, 0) + 1
            # recurse
            dfs(node.left, current)
            dfs(node.right, current)
            # path sum is no longer valid decrement frequency
            cache[current] -= 1
        dfs(root, 0)
        return answer

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)