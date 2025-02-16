# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, find a sequence that satisfies all of the following:
    * The integer 1 occurs once in the sequence.
    * Each integer between 2 and n occurs twice in the sequence.
    * For every integer i between 2 and n, the distance between the two
      occurrences of i is exactly i.

    The distance between two number on the sequence, a[i] and a[j] is the
    absolute difference of their indices, abs(j-i).

    Return the lexicographically largest sequence. It is guaranteed that under
    the given constraints, there is always a solution.
    '''
    def constructDistancedSequence(self, n: int) -> List[int]:
        answer = [0] * (2 * n - 1)
        def r(i: int) -> bool:
            if i == len(answer):
                return True
            if answer[i] != 0:
                return r(i+1)
            for x in range(n, 1, -1):
                if x not in answer and answer[i] == 0 and i + x < len(answer) and answer[i+x] == 0:
                    answer[i] = x
                    answer[i+x] = x
                    if r(i+1):
                        return True
                    answer[i] = 0
                    answer[i+x] = 0
            if 1 not in answer:
                answer[i] = 1
                if r(i+1):
                    return True
                answer[i] = 0
            return False
        r(0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = [3,1,2,3,2]
        self.assertEqual(s.constructDistancedSequence(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = [5,3,1,4,3,5,2,4,2]
        self.assertEqual(s.constructDistancedSequence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)