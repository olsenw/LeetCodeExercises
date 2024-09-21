# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return all the numbers in the range [1,n] sorted in
    lexicographical order.

    Write an algorithm that runs in O(n) time and uses O(1) space.
    '''
    # O(n log n) time
    def lexicalOrder_invalid(self, n: int) -> List[int]:
        return [int(s) for s in sorted(str(i) for i in range(1,n+1))]

    # based on leetcode dfs solution
    # https://leetcode.com/problems/lexicographical-numbers/editorial/?envType=daily-question&envId=2024-09-21
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []
        def dfs(i):
            if i > n:
                return
            answer.append(i)
            for j in range(10):
                k = i * 10 + j
                if k > n:
                    return
                dfs(k)
            return
        for i in range(1, 10):
            dfs(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13
        o = [1,10,11,12,13,2,3,4,5,6,7,8,9]
        self.assertEqual(s.lexicalOrder(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = [1,2]
        self.assertEqual(s.lexicalOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)