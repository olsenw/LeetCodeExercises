# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of n strings sts, all or the same length.

    The strings can be arranged such that there is one on each line, making a
    grid.

    Delete the columns that not sorted lexicographically.

    Return the number of columns that will be deleted
    '''
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        m,n = len(strs), len(strs[0])
        for j in range(n):
            o = ord(strs[0][j])
            for i in range(m):
                if ord(strs[i][j]) < o:
                    answer += 1
                    break
                o = ord(strs[i][j])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["cba","daf","ghi"]
        o = 1
        self.assertEqual(s.minDeletionSize(i), o)

    def test_two(self):
        s = Solution()
        i = ["a","b"]
        o = 0
        self.assertEqual(s.minDeletionSize(i), o)

    def test_three(self):
        s = Solution()
        i = ["zyx","wvu","tsr"]
        o = 3
        self.assertEqual(s.minDeletionSize(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)