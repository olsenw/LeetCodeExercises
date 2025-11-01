# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string target.

    Alice is going to type target on their computer using a special keyboard
    that has only two keys:
    * Key 1 appends the character "a" to the string on the screen.
    * Key 2 changes the last character of the string on the screen to its
      character in the English alphabet.
    
    Note that initially there is an empty string "" on the screen, so only key 1
    can be pressed.

    Return a list of all strings that appear on the screen as Alice types
    target, in the order they appear, using the minimum key presses.
    '''
    def stringSequence(self, target: str) -> List[str]:
        answer = [chr(c) for c in range(ord('a'), ord(target[0])+1)]
        for i in target[1:]:
            app = answer[-1]
            for j in range(ord('a'), ord(i)+1):
                answer.append(app + chr(j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = ["a","aa","ab","aba","abb","abc"]
        self.assertEqual(s.stringSequence(i), o)

    def test_two(self):
        s = Solution()
        i = "he"
        o = ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
        self.assertEqual(s.stringSequence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)