# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A teacher is writing a test with n true/false questions, with 'T' denoting
    true and 'F' denoting false. They want to confuse the students by maximizing
    the number of consecutive questions with the same answer (multiple trues or
    multiple falses in a row).

    Given a string answerKey, where answerKey[i] is the original answer to the
    ith question. In addition, an integer k is also given, the maximum number of
    times it is possible to preform the following operation.

    * Change the answer key for any question to 'T' or 'F' (ie set answerKey[i]
      to 'T' or 'F').

    Return the maximum number of consecutive 'T's or 'F's in the answer key
    after performing the operation at most k times.
    '''
    def maxConsecutiveAnswers_brute(self, answerKey: str, k: int) -> int:
        def scan(c):
            answer = 0
            for i in range(len(answerKey)):
                f = 0
                l = 0
                for j in range(i, len(answerKey)):
                    if answerKey[j] != c:
                        f += 1
                    if f > k:
                        break
                    l += 1
                answer = max(answer, l)
            return answer
        return max(scan('T'), scan('F'))

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def scan(c):
            answer = 0
            # target answer, not target answer
            w = [0, 0]
            left = 0
            for right in range(len(answerKey)):
                if answerKey[right] == c:
                    w[0] += 1
                else:
                    w[1] += 1
                while w[1] > k and left < right :
                    if answerKey[left] == c:
                        w[0] -= 1
                    else:
                        w[1] -= 1
                    left += 1
                if w[1] <= k:
                    answer = max(answer, sum(w))
            return answer
        return max(scan('T'), scan('F'))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "TTFF"
        j = 2
        o = 4
        self.assertEqual(s.maxConsecutiveAnswers(i,j), o)

    def test_two(self):
        s = Solution()
        i = "TFFT"
        j = 1
        o = 3
        self.assertEqual(s.maxConsecutiveAnswers(i,j), o)

    def test_three(self):
        s = Solution()
        i = "TTFTTFTT"
        j = 1
        o = 5
        self.assertEqual(s.maxConsecutiveAnswers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)