# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words and a width maxWidth, format the text such
    that each line has exactly maxWidth characters and is fully (left and right)
    justified.

    Words should be packed in a greedy approach; that is, pack as many words as
    possible in each line. Pad extra ' ' when necessary so that each line has
    exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If
    the number of spaces on a line does not divide evenly between words, the
    empty slots on the left will be assigned more spaces than the slots on the
    right.

    For the last line of text, it should be left-justified, and no extra space
    is inserted between words.

    Note:
    * A word is defined as a character sequence consisting of non-space 
      characters only.
    * Each word's length is guaranteed to be greater than 0 and not exceed
      maxWidth.
    * The input array words contains at least one word.
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        i = 0
        while i < len(words):
            line = [words[i]]
            c = maxWidth - len(words[i])
            i += 1
            while i < len(words) and c - 1 - len(words[i]) >= 0:
                line.append(" ")
                line.append(words[i])
                c -= 1 + len(words[i])
                i += 1
            if i == len(words):
                answer.append(''.join(line))
                break
            while c and len(line) > 1:
                j = 1
                while c and j < len(line):
                    line[j] += " "
                    c -= 1
                    j += 2
            if len(line) == 1:
                line.append(" " * (maxWidth - len(line[-1])))
            answer.append(''.join(line))
        answer[-1] += " " * (maxWidth - len(answer[-1]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["This", "is", "an", "example", "of", "text", "justification."]
        j = 16
        o = [
                "This    is    an",
                "example  of text",
                "justification.  "
            ]
        self.assertEqual(s.fullJustify(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["What","must","be","acknowledgment","shall","be"]
        j = 16
        o = [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ]
        self.assertEqual(s.fullJustify(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        j = 20
        o = [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  "
            ]
        self.assertEqual(s.fullJustify(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)