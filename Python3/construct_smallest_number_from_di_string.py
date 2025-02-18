# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string patter of length n consisting of the characters 'I'
    meaning increasing and 'D' meaning decreasing.

    A 0-indexed string num of length n + 1 is created using the following
    conditions:
    * num consists of the digits '1' to '9', where each digit is used at most
      once.
    * If pattern[i] == 'I', then num[i] < num[i + 1].
    * If pattern[i] == 'D', then num[i] > num[i + 1].

    Return the lexicographically smallest possible string num that meets the
    conditions.
    '''
    # bad indexing
    def smallestNumber_fails(self, pattern: str) -> str:
        n = len(pattern) + 1
        answer = [0] if pattern[0] == 'I' else [10]
        def backtrack(l):
            if l == n:
                return True
            for d in range(1,9):
                if d not in answer and ((pattern[l] == 'D' and d < answer[-1]) or (pattern[l] == 'I' and d > answer[-1])):
                    answer.append(d)
                    if backtrack(l+1):
                        return True
                    answer.pop()
            return False
        backtrack(0)
        return int(''.join(answer[1:]))

    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        answer = []
        def backtrack(index):
            if index == n+1:
                return True
            for i in range(1,10):
                if i not in answer and \
                   (
                       (pattern[index-1] == 'D' and i < answer[-1]) or
                       (pattern[index-1] == 'I' and i > answer[-1])
                   ):
                    answer.append(i)
                    if backtrack(index+1):
                        return True
                    answer.pop()
            return False
        for i in range(1,10):
            answer = [i]
            if backtrack(1):
                return ''.join(str(j) for j in answer)
        return 'None'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "IIIDIDDD"
        o = "123549876"
        self.assertEqual(s.smallestNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "DDD"
        o = "4321"
        self.assertEqual(s.smallestNumber(i), o)

    def test_three(self):
        s = Solution()
        i = "II"
        o = "123"
        self.assertEqual(s.smallestNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)