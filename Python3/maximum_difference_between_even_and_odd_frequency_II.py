# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k. Find the maximum difference between the
    frequency of two charactesr, freq[a] - freq[b], in a substring subs of s,
    such that:
    * subs has a size of at least k.
    * Character a has an odd frequency in subs.
    * Character b has an even frequency in subs

    Return the maximum difference.

    Note that subs can contain more than 2 distinct characters.
    '''
    # O(n^2)
    def maxDifference_brute(self, s: str, k: int) -> int:
        answer = -10**7-9
        prefix = [[0] * 5]
        for c in s:
            p = [i for i in prefix[-1]]
            p[ord(c) - 48] += 1
            prefix.append(p)
        for w in range(k, len(s)+1):
            for i in range(w, len(s)+1):
                c = [prefix[i][j] - prefix[i-w][j] for j in range(5)]
                for even in range(5):
                    for odd in range(5):
                        if c[odd] and c[even] and c[odd] % 2 == 1 and c[even] % 2 == 0:
                            answer = max(answer, c[odd] - c[even])
                            pass
                pass
        return answer

    # does not consider unneeded character, which substrings may require filler
    # characters to maintain length requirement.
    def maxDifference_fails(self, s: str, k: int) -> int:
        def helper(a:str, b:str) -> int:
            answer = -10**9 - 7
            prefix = [[0,0]]
            for c in s:
                if c == a:
                    prefix.append([prefix[-1][0] + 1, prefix[-1][1]])
                if c == b:
                    prefix.append([prefix[-1][0], prefix[-1][1] + 1])
            pass
            for i in range(len(prefix)):
                for j in range(i + k, len(prefix)):
                    a = prefix[j][0] - prefix[i][0]
                    b = prefix[j][1] - prefix[i][1]
                    if a % 2 == b % 2:
                        continue
                    if a % 2:
                        answer = max(answer, a - b)
                    else:
                        answer = max(answer, b - a)
            return answer
        answer = -10**9 - 7
        for i in range(5):
            for j in range(i+1,5):
                a,b = chr(48 + i), chr(48 + j)
                answer = max(answer, helper(a,b))
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/editorial/?envType=daily-question&envId=2025-06-11
    def maxDifference(self, s: str, k: int) -> int:
        # determine which of four states the counts are in
        # 00 -> even number of a and b
        # 01 -> even number of a, odd number of b
        # 10 -> odd number of a, even number of b
        # 11 -> odd number of a, odd number of b
        # note only case 10 is valid for consideration in wider problem scope
        def status(acount:int, bcount:int) -> int:
            return ((acount & 1) << 1) | (bcount & 1)
        n = len(s)
        answer = -10**7 - 9
        # try character as odd
        for a in "01234":
            # try character as even
            for b in "01234":
                # must be different characters
                if a == b:
                    continue
                best = [10**7+9] * 4
                acount, bcount = 0,0
                aprev, bprev = 0,0
                left = -1
                for right in range(n):
                    acount += s[right] == a
                    bcount += s[right] == b
                    # windows must be minimum size
                    # even number (b) must have at least 2 occurrences
                    # shrink
                    while right - left >= k and bcount - bprev >= 2:
                        leftstatus = status(aprev, bprev)
                        # best answer so far for given status code
                        best[leftstatus] = min(best[leftstatus], aprev - bprev)
                        left += 1
                        aprev += s[left] == a
                        bprev += s[left] == b
                    # compute current window status
                    rightstatus = status(acount, bcount)
                    # if valid case
                    if best[rightstatus ^ 0b10] != 10**7+9:
                        # best answer so far for given status code in window
                        answer = max(answer, acount - bcount - best[rightstatus ^ 0b10])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "12233"
        j = 4
        o = -1
        self.assertEqual(s.maxDifference(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1122211"
        j = 3
        o = 1
        self.assertEqual(s.maxDifference(i,j), o)

    def test_three(self):
        s = Solution()
        i = "110"
        j = 3
        o = -1
        self.assertEqual(s.maxDifference(i,j), o)

    def test_four(self):
        s = Solution()
        i = "44114402"
        j = 7
        o = 1
        self.assertEqual(s.maxDifference(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)