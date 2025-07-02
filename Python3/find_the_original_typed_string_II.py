# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice is attempting to type a specific string on their computer. However,
    she tends to be clumsy and may press a key for too long, resulting in a
    character being typed multiple times.

    Given a string word, which represents the final output displayed on Alice's
    screen. Also given is a positive integer k.

    Return the total number of possible original strings that Alice might have
    intended to type, if she was trying to type a string of size at least k.

    Since the answer may be very large, return it modulo 1o^9 + 7.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/find-the-original-typed-string-ii/editorial/?envType=daily-question&envId=2025-07-02
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        modulo = 10**9 + 7
        count = 1
        # get a frequency of each sequential character in word
        freq = list()
        for i in range(1,n):
            if word[i] == word[i-1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)
        #
        answer = 1
        for i in freq:
            answer = (answer * i) % modulo
        # more than k letters, so all cases covered by multiplication
        if len(freq) >= k:
            return answer
        # calculate all cases using less than k letters
        f = [1] + [0] * (k-1)
        g = [1] * k
        for i in range(len(freq)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % modulo
            g_new = [f_new[0]] + [0] * (k-1)
            for j in range(1,k):
                g_new[j] = (g_new[j-1] + f_new[j]) % modulo
            f = f_new
            g = g_new
        # subtract all cases of less than k letters from total outputs
        return (answer - g[k-1]) % modulo

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabbccdd"
        j = 7
        o = 5
        self.assertEqual(s.possibleStringCount(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aabbccdd"
        j = 8
        o = 1
        self.assertEqual(s.possibleStringCount(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaabbb"
        j = 3
        o = 8
        self.assertEqual(s.possibleStringCount(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)