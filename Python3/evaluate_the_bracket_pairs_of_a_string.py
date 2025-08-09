# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s that contains some bracket pairs, with each pair containing
    a non-empty key.

    The values of a wide range of keys are know. This is represented by a 2D
    string array knowledge where each knowledge[i] = [keyi, valuei] indicates
    that keyi has a value of valuei.

    Evaluate all of the bracket pairs. When evaluating a bracket pair that
    contains some key keyi:
    * Replace keyi and the bracket pair with the key's corresponding valuei.
    * If the value of the key is unknown, replace keyi and the bracket pair with
      a question mark "? (without the quotation marks).
    
    Each key will appear at most once in knowledge. There will not be any nested
    brackets in s.

    Return the resulting string after evaluating all of the bracket pairs.
    '''
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {i:j for i,j in knowledge}
        stack = [""]
        for c in s:
            if c =='(':
                stack.append("")
            elif c == ')':
                v = stack.pop()
                if v in knowledge:
                    stack[-1] += knowledge[v]
                else:
                    stack[-1] += '?'
            else:
                stack[-1] += c
        return stack.pop()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(name)is(age)yearsold"
        j = [["name","bob"],["age","two"]]
        o = "bobistwoyearsold"
        self.assertEqual(s.evaluate(i,j), o)

    def test_two(self):
        s = Solution()
        i = "hi(name)"
        j = [["a","b"]]
        o = "hi?"
        self.assertEqual(s.evaluate(i,j), o)

    def test_three(self):
        s = Solution()
        i = "(a)(a)(a)aaa"
        j = [["a","yes"]]
        o = "yesyesyesaaa"
        self.assertEqual(s.evaluate(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)