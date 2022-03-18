# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, remove duplicate letters so that every letter
    appears once and only once. Return the result that is the smallest
    lexicographical order of all possible results.
    '''
    # based on solution by DBabichev
    # https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O(n)-greedy-with-stack-explained
    def removeDuplicateLetters(self, s: str) -> str:
        # monotonic stack
        stack = []
        # last index for every letter in the string
        indices = {c:i for i,c in enumerate(s)}
        # letters already on stack
        contain = set()
        for i,c in enumerate(s):
            # check if already have letter
            if c not in contain:
                # monotonicity increasing stack (ish letter order trumps)
                # empty stack | lesser lex order | possible to re-add later
                while stack and c < stack[-1] and i < indices[stack[-1]]:
                    contain.discard(stack.pop())
                stack.append(c)
                contain.add(c)
        return ''.join(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bcabc"
        o = "abc"
        self.assertEqual(s.removeDuplicateLetters(i), o)

    def test_two(self):
        s = Solution()
        i = "cbacdcbc"
        o = "acdb"
        self.assertEqual(s.removeDuplicateLetters(i), o)

    def test_three(self):
        s = Solution()
        i = "caaaacbbbc"
        o = "abc"
        self.assertEqual(s.removeDuplicateLetters(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)