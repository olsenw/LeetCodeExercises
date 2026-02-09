# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D string array responses where responses[i] is an array of strings
    representing responses from the ith day.

    Return the most common response across all days after removing duplicate
    responses within each responses[i]. If there is a tie, return the
    lexicograpically smallest response.
    '''
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c = Counter()
        for r in responses:
            c.update(set(r))
        answer = "z"*1000
        m = 0
        for a,x in c.most_common():
            if x >= m:
                answer = min(answer, a)
                m = x
            else:
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
        o = "good"
        self.assertEqual(s.findCommonResponse(i), o)

    def test_two(self):
        s = Solution()
        i = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
        o = "bad"
        self.assertEqual(s.findCommonResponse(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)