# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums of length n, and an integer array queries of
    length m.

    Return an array answer of length m where answer[i] is the maximum size of a
    subsequence that can be taken from nums such that the sum of its elements is
    less than or equal to queries[i].

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    '''
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        for q in queries:
            s,a = 0, 0
            for n in nums:
                if s + n > q:
                    break
                s += n
                a += 1
            answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,5,2,1]
        j = [3,10,21]
        o = [2,3,4]
        self.assertEqual(s.answerQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,5]
        j = [1]
        o = [0]
        self.assertEqual(s.answerQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)