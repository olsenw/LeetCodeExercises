# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word and a non-negative integer k.

    Return the total number of substrings of word that contain every vowel
    (aeiou) at least once and exactly k consonants
    '''
    def countOfSubstrings_brute(self, word: str, k: int) -> int:
        n = len(word)
        answer = 0
        for i in range(n):
            vowel = [0] * 5
            consonants = 0
            for j in range(i, n):
                if word[j] == 'a': vowel[0] += 1
                elif word[j] == 'e': vowel[1] += 1
                elif word[j] == 'i': vowel[2] += 1
                elif word[j] == 'o': vowel[3] += 1
                elif word[j] == 'u': vowel[4] += 1
                else: consonants += 1
                if consonants == k and all(v > 0 for v in vowel):
                    answer += 1
                elif consonants > k:
                    break
        return answer

    # based on Leetcode solution sliding window relaxed constraints
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastK(k:int)->int:
            answer = 0
            start,end = 0,0
            vowel = dict()
            consonant = 0
            while end < len(word):
                letter = word[end]
                if letter in "aeiou":
                    if letter in vowel:
                        vowel[letter] += 1
                    else:
                        vowel[letter] = 1
                else:
                    consonant += 1
                while len(vowel) == 5 and consonant >= k:
                    answer += len(word) - end
                    letter = word[start]
                    if letter in "aeiou":
                        if vowel[letter] > 1:
                            vowel[letter] -= 1
                        else:
                            del vowel[letter]
                    else:
                        consonant -= 1
                    start += 1
                end += 1
            return answer
        return atLeastK(k) - atLeastK(k+1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aeioqq", 1
        o = 0
        self.assertEqual(s.countOfSubstrings(*i), o)

    def test_two(self):
        s = Solution()
        i = "aeiou", 0
        o = 1
        self.assertEqual(s.countOfSubstrings(*i), o)

    def test_three(self):
        s = Solution()
        i = "ieaouqqieaouqq", 1
        o = 3
        self.assertEqual(s.countOfSubstrings(*i), o)

    def test_three(self):
        s = Solution()
        i = "aaaeiouuu", 0
        o = 9
        self.assertEqual(s.countOfSubstrings(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)