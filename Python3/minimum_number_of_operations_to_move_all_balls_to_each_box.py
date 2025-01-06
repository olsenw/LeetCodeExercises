# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n boxes. Given a binary string boxes of length n, where boxes[i]
    is '0' if the ith box is empty, and '1' if it contains one ball.

    In one operation, it is possible to move one ball from a box to an adjacent
    box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing
    so, there may be more than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of
    operations needed to move all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.
    '''
    # prefix sum math is wrong
    # need to adjust math
    def minOperations_wrong(self, boxes: str) -> List[int]:
        n = len(boxes)
        p = [0] * len(boxes)
        for i in range(n-2,-1,-1):
            p[i] = (boxes[i+1] == '1') + p[i+1]
        answer = [p[0]]
        s = 0
        for i in range(1,n):
            s += s + (boxes[i-1] == '1')
            answer.append(s + p[i])
        return answer

    # based on hints (very slow)
    def minOperations_brute(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []
        for i in range(n):
            a = 0
            for j in range(n):
                if boxes[j] == '1':
                    a += abs(i - j)
            answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "110"
        o = [1,1,3]
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = "001011"
        o = [11,8,5,4,3,4]
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)