# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and target, both having length n, consisting of
    lowercase English letters.

    Return the lexicographically smallest permutation of s that is strictly
    greater than target. If no permutation of s is lexicographically strictly
    greater than target, return an empty string.
    '''
    # does not handle corner cases correctly
    def lexGreaterPermutation_fails(self, s: str, target: str) -> str:
        c = Counter(s)
        answer = ''
        for i in target:
            if i in c and c[i]:
                answer += i
                c[i] -= 1
            else:
                for j in range(ord(i)+1,ord('z')+1):
                    j = chr(j)
                    if j in c and c[j]:
                        answer += j
                        c[j] -= 1
                        break
                else:
                    # unable to find lexicographically greater character
                    return ""
                # mus have found character that is strictly greater
                break
        if answer == target:
            for i in answer[::-1]:
                c[i] += 1
                answer = answer[:-1]
                for j in range(ord(i)+1,ord('z')+1):
                    j = chr(j)
                    if j in c and c[j]:
                        answer += j
                        c[j] -= 1
                        break
                else:
                    # backtrack,
                    continue
                break
            else:
                # unable to find lexicographically greater character
                return ""
        if len(answer) == 0:
            return ""
        for i in "abcdefghijklmnopqrstuvwxyz":
            answer += i * c[i]
        return answer

    def lexGreaterPermutation_incomplete(self, s: str, target: str) -> str:
        c = Counter(s)
        answer = ""
        for i,j in enumerate(target):
            # have the letter attach to answer
            if j in c and c[j]:
                answer += j
                c[j] -= 1
            # try placing the next largest letter
            else:
                for k in range(ord(j)+1,ord('z')+1):
                    k = chr(k)
                    if k in c and c[k]:
                        answer += k
                        c[k] -= 1
                        break
                else:
                    # need to backtrack
                    continue
                break
        for i in "abcdefghijklmnopqrstuvwxyz":
            answer += i * c[i]
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/editorial/?envType=daily-question&envId=2026-08-27
    # having trouble formulating code flow on own :(
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        c = Counter(s)
        answer = ""
        for i,j in enumerate(target):
            # try placing the character at this position in target
            if c[j]:
                c[j] -= 1
                # test if larger suffix exists (means keep this letter)
                m = "".join(k * c[k] for k in reversed("abcdefghijklmnopqrstuvwxyz"))
                if m > target[i+1:]:
                    answer += j
                    continue
                c[j] += 1
            # try placing a larger character
            for k in range(ord(j)+1, ord('z')+1):
                k = chr(k)
                if c[k]:
                    c[k] -= 1
                    answer += k
                    # append rest of characters sorted
                    for key in sorted(c.keys()):
                        answer += key * c[key]
                    return answer
            # no possible answer
            return ""
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "bba"
        o = "bca"
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

    def test_two(self):
        s = Solution()
        i = "leet"
        j = "code"
        o = "eelt"
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

    def test_three(self):
        s = Solution()
        i = "baba"
        j = "bbaa"
        o = ""
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

    def test_four(self):
        s = Solution()
        i = "abfde"
        j = "abbcd"
        o = "abdef"
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

    def test_five(self):
        s = Solution()
        i = "ab"
        j = "ab"
        o = "ba"
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

    def test_six(self):
        s = Solution()
        i = "aab"
        j = "abb"
        o = "baa"
        self.assertEqual(s.lexGreaterPermutation(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)