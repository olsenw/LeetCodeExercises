# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, partition s such that every substring of the
    partition is a palindrome. Return all possible palindrome
    partitioning of s.

    A palindrome string is a string that reads the same backward as
    forward.
    '''
    def partition_dfs(self, s: str) -> List[List[str]]:
        # check is string [start, stop] is a palindrome
        def is_palindrome(start: int, stop: int) -> bool:
            while start < stop:
                if s[start] != s[stop]:
                    return False
                start += 1
                stop -= 1
            return True
        # variable to hold list we wish to return
        answer = []
        current = []
        # depth first search
        def dfs(start:int, answer: List[List[str]], current: List[str]):
            # base case (no more partitions)
            if start >= len(s):
                answer.append(list(current))
            # generate partitions
            for stop in range(start, len(s)):
                if is_palindrome(start, stop):
                    current.append(s[start:stop+1])
                    dfs(stop+1, answer, current)
                    current.pop()
        # start recursive search
        dfs(0, answer, current)
        return answer

    # misunderstood examples partitioning
    def partition_fail(self, s: str) -> List[List[str]]:
        def palindrome(start, stop) -> bool:
            l = stop - start + 1
            for i in range(l//2):
                if s[start + i] != s[stop - i]:
                    return False
            return True
        ans = []
        # length of partitions
        for i in range(1, len(s)+1):
            sub = []
            # check subpartitions
            start = 0
            while start < len(s):
                stop = start + i - 1
                if stop >= len(s):
                    stop = len(s) - 1
                if palindrome(start, stop):
                    sub.append(s[start:stop+1])
                start += i
            if sub:
                ans.append(sub)
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aab"
        o = [["a","a","b"],["aa","b"]]
        self.assertEqual(s.partition_dfs(i), o)

    def test_two(self):
        s = Solution()
        i = "a"
        o = [["a"]]
        self.assertEqual(s.partition_dfs(i), o)

    def test_three(self):
        s = Solution()
        i = "aaa"
        o = [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]
        self.assertEqual(s.partition_dfs(i), o)

    def test_four(self):
        s = Solution()
        i = "cdd"
        o = [["c","d","d"],["c","dd"]]
        self.assertEqual(s.partition_dfs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)