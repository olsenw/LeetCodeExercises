# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of string words, return all strings in words that is a
    substring of another word. The answer can be returned in any order.

    A substring is a contiguous sequence of characters within a string.
    '''
    # small problem space, brute force
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        # words.sort(key=lambda x: len(x))
        n = len(words)
        for i in range(n):
            for j in range(n):
            # for j in range(i+1,n):
                if i != j and words[i] in words[j]:
                    answer.append(words[i])
                    break
                # if len(words[i]) < len(words[j]) and words[i] in words[j]:
                #     answer.append(words[i])
                #     break
                # elif len(words[i]) >= len(words[j]) and words[j] in words[i]:
                #     answer.append(words[j])
                #     break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["mass","as","hero","superhero"]
        o = ["as","hero"]
        self.assertEqual(s.stringMatching(i), o)

    def test_two(self):
        s = Solution()
        i = ["leetcode","et","code"]
        o = ["et","code"]
        self.assertEqual(s.stringMatching(i), o)

    def test_three(self):
        s = Solution()
        i = ["leetcoder","leetcode","od","hamlet","am"]
        o = ["leetcode","od","am"]
        self.assertEqual(s.stringMatching(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)