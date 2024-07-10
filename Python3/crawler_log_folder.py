# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The Leetcode file system keeps a log each time some user performs a change
    folder operation.

    The operations are described below:
    * "../": Move to the parent folder of the current folder. (If already in the
      main folder, remain in the same folder).
    * "./": Remain in the same folder.
    * "x/": Move to the child folder named x (Which is guaranteed to exist).

    Given a list of strings logs where logs[i] is the operation performed by the
    user at the ith step.

    The file system starts in the main folder, then the operations in logs are
    performed.

    Return the minimum number of operations needed to go back to the main folder
    after the change folder operations.
    '''
    def minOperations(self, logs: List[str]) -> int:
        a = 0
        for l in logs:
            if l == "../":
                if a > 0:
                    a -= 1
            elif l == "./":
                pass
            else:
                a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["d1/","d2/","../","d21/","./"]
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = ["d1/","d2/","./","d3/","../","d31/"]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = ["d1/","../","../","../"]
        o = 0
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = ["./","../","./"]
        o = 0
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)