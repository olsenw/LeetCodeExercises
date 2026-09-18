# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of lowercase letters, find the maximum number of non-empty
    substrings of s that meet the following conditions:
    1. The substrings do not overlap, that is for any two substrings s[i..j]
       and s[x..y], either j < x or i > y is true.
    2. A substring that contains a certain character c must also contain all
       occurrences of c.
    
    Find the maximum number of substrings that meet the above conditions. If
    there are multiple solutions with the same number of substrings, return the
    one with minimum total length. It can be shown that there exists a unique
    solution of minimum total length.

    Notice that the substrings can be returned in any order.
    '''
    def maxNumOfSubstrings_incorrect(self, s: str) -> list[str]:
        starts = dict()
        ends = defaultdict()
        for i,j in enumerate(s):
            if j not in starts:
                starts[j] = i
            ends[j] = i
        possible = []
        for i in starts:
            # hint 1) it is only possible for two substrings to overlap is if one fully contains the other
            length = 0
            start = starts[i]
            end = ends[i]
            chars = "".join(i for i in starts if start <= starts[i] <= ends[i] <= end)
            pass
            while length < end - start + 1:
                length = end - start + 1
                for j in starts:
                    a,b = starts[j],ends[j]
                    if a < start < b < end:
                        start = a
                        chars += s[start]
                    if start < a < end < b:
                        end = b
                        chars += s[end]
            possible.append((start, end, chars))
        possible.sort(key=lambda x:(x[1]-x[0]+1,x[2]))
        answer = []
        taken = ""
        for i,j,k in possible:
            if any(c in k for c in taken):
                continue
            answer.append(s[i:j+1])
            taken += k
        return answer

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        c = Counter(s)
        starts = dict()
        ends = defaultdict()
        for i,j in enumerate(s):
            if j not in starts:
                starts[j] = i
            ends[j] = i
        possible = []
        for i in starts:
            # hint 1) it is only possible for two substrings to overlap is if one fully contains the other
            length = 0
            start = starts[i]
            end = ends[i]
            chars = "".join(i for i in starts if start <= starts[i] <= ends[i] <= end)
            pass
            while length < end - start + 1:
                length = end - start + 1
                for j in starts:
                    a,b = starts[j],ends[j]
                    if a < start < b < end:
                        start = a
                        chars += s[start]
                    if start < a < end < b:
                        end = b
                        chars += s[end]
            chars = "".join(i for i in starts if start <= starts[i] <= ends[i] <= end)
            if end-start+1 == sum(c[x] for x in chars):
                possible.append((start, end, chars))
        possible.sort(key=lambda x:(x[1]-x[0]+1,x[2]))
        answer = []
        taken = ""
        for i,j,k in possible:
            if any(c in k for c in taken):
                continue
            answer.append(s[i:j+1])
            taken += k
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "adefaddaccc"
        o = sorted(["e","f","ccc"])
        self.assertEqual(sorted(s.maxNumOfSubstrings(i)), o)

    def test_two(self):
        s = Solution()
        i = "abbaccd"
        o = sorted(["d","bb","cc"])
        self.assertEqual(sorted(s.maxNumOfSubstrings(i)), o)

    def test_three(self):
        s = Solution()
        i = "ababa"
        o = sorted(["ababa"])
        self.assertEqual(sorted(s.maxNumOfSubstrings(i)), o)

    def test_four(self):
        s = Solution()
        i = "wvwppcieodxgwgilrtmmdjtviiuqbrtllevmzolaxbwlnftdhnhdnhwlccgfgaqqylazvxxscembaqbqsxqykneptybxklnabifqssaqwxxzmvsfavjuhzznkicopfmzcfihvgjbyhmieyglihytxibhmxzxusmvhjyp"
        o = sorted(["wvwppcieodxgwgilrtmmdjtviiuqbrtllevmzolaxbwlnftdhnhdnhwlccgfgaqqylazvxxscembaqbqsxqykneptybxklnabifqssaqwxxzmvsfavjuhzznkicopfmzcfihvgjbyhmieyglihytxibhmxzxusmvhjyp"])
        self.assertEqual(sorted(s.maxNumOfSubstrings(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)