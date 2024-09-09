# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Given two integers m and n, which represent the dimensions of a matrix.

    Also given is the head of a linked list of integers.

    Generate an m x n matrix that contains the integers in the linked list
    presented in spiral order (clockwise), starting from the top-left of the
    matrix. If there are remaining empty spaces, fill them with -1.

    Return the generated matrix.
    '''
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr = head
        answer = [[-1] * n for _ in range(m)]
        a,b = 0,0
        while curr:
            i,j = a,b
            for j in range(b,n):
                if curr is None:
                    return answer
                answer[i][j] = curr.val
                curr = curr.next
            n -= 1
            for i in range(a+1,m):
                if curr is None:
                    return answer
                answer[i][j] = curr.val
                curr = curr.next
            a += 1
            for j in range(n-1,b-1,-1):
                if curr is None:
                    return answer
                answer[i][j] = curr.val
                curr = curr.next
            m -= 1
            for i in range(m-1,a-1,-1):
                if curr is None:
                    return answer
                answer[i][j] = curr.val
                curr = curr.next
            b += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3, 5, ListNode(3, ListNode(0, ListNode(2, ListNode(6, ListNode(8, ListNode(1, ListNode(7, ListNode(9, ListNode(4, ListNode(2, ListNode(5, ListNode(5, ListNode(0)))))))))))))
        o = [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
        self.assertEqual(s.spiralMatrix(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)