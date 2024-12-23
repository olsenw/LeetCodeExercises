# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
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
    Given the root of a binary with unique values.

    In one operation, choose any two nodes at the same level and swap their
    values.

    Return the minimum number of operations needed to make the values at each
    level sorted in a strictly increasing order.

    The level of a node is the number of edges along the path between it and the
    root node.
    '''
    # assumption on swaps needed incorrect
    # 20,46,15,39 require three swaps
    def minimumOperations_fails(self, root: Optional[TreeNode]) -> int:
        answer = 0
        curr = [root]
        next = [root]
        while curr:
            heap = []
            curr = next
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                    heapq.heappush(heap, node.left.val)
                if node.right:
                    next.append(node.right)
                    heapq.heappush(heap, node.right.val)
            oops = sum(node.val != heapq.heappop(heap) for node in next)
            answer += oops // 2 + oops % 2
        return answer

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        answer = 0
        curr = [root]
        next = [root]
        while curr:
            heap = []
            curr = next
            next = []
            indices = dict()
            values = dict()
            index = 0
            for node in curr:
                if node.left:
                    next.append(node.left)
                    heapq.heappush(heap, node.left.val)
                    indices[index] = node.left.val
                    values[node.left.val] = index
                    index += 1
                if node.right:
                    next.append(node.right)
                    heapq.heappush(heap, node.right.val)
                    indices[index] = node.right.val
                    values[node.right.val] = index
                    index += 1
            for i in range(index):
                j = heapq.heappop(heap)
                if indices[i] != j:
                    answer += 1
                    a,b = indices[i], values[indices[i]]
                    c,d = indices[values[j]], values[j]
                    indices[b], values[a] = c,d
                    indices[d], values[c] = a,b
                    pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = TreeNode(1, TreeNode(4, TreeNode(7), TreeNode(6)), TreeNode(3, TreeNode(8, TreeNode(9)), TreeNode(5, TreeNode(10))))
        o = 3
        self.assertEqual(s.minimumOperations(i), o)

    def test_two(self):
        s = Solution()
        i = TreeNode(1, TreeNode(3, TreeNode(7), TreeNode(6)), TreeNode(2, TreeNode(5), TreeNode(4)))
        o = 3
        self.assertEqual(s.minimumOperations(i), o)

    def test_three(self):
        s = Solution()
        i = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        o = 0
        self.assertEqual(s.minimumOperations(i), o)

    def test_four(self):
        s = Solution()
        i = TreeNode(49, TreeNode(45, TreeNode(20, TreeNode(27)), TreeNode(46)), TreeNode(1, TreeNode(15, TreeNode(25)), TreeNode(39)))
        o = 5
        self.assertEqual(s.minimumOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)