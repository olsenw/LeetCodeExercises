# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In an infinite binary tree where every node has two children, the nodes are
    labelled in row order.

    In the odd numbered rows (ie, the first, third, fifth, ...) the labelling is
    left to right, while in the even numbered rows (second, fourth, sixth, ...),
    the labelling is right to left.

    Given the label of a node in this tree, return the labels in the path from
    the root of the tree to the node with that label.
    '''
    # brute force
    # builds the tree, then backtracks
    def pathInZigZagTree_brute(self, label: int) -> List[int]:
        answer = []
        row = 0
        while 2**row <= label:
            row += 1
        tree = [[1]]
        for i in range(1,row):
            last = tree[-1][-1] + 1
            tree.append([])
            for j in range(2**(i)):
                tree[-1].append(last + j)
        for i in range(1,row,2):
            tree[i] = tree[i][::-1]
        index = tree[-1].index(label)
        while len(tree) > 0:
            answer.append(tree[-1][index])
            tree.pop()
            index //= 2
        return answer[::-1]

    # based on code sample for 0ms
    # uses the power of math
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log(label, 2))
        answer = list()
        for i in  range(level, -1, -1):
            answer.append(label)
            label = (3 * (2 ** i) - 1 - label) // 2
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 14
        o = [1,3,4,14]
        self.assertEqual(s.pathInZigZagTree(i), o)

    def test_two(self):
        s = Solution()
        i = 26
        o = [1,2,6,10,26]
        self.assertEqual(s.pathInZigZagTree(i), o)

    def test_three(self):
        s = Solution()
        i = 16
        o = [1,3,4,15,16]
        self.assertEqual(s.pathInZigZagTree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)