# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string formula representing a chemical formula, return the count of
    each atom.

    The atomic element always starts with an uppercase character, then zero or
    more lowercase letters, representing the name.

    One or more digits representing that element's count may follow if the count
    is greater than 1. If the count is 1, no digits will follow.

    Two formulas are concatenated together to produce another formula.

    A formula places in parentheses, and a count (optionally added) is also a
    formula.

    Return the count of all elements as a string in the following form: the
    first name (in sorted order), followed by its count (if that count is more
    than 1), followed by the second name (in sorted order), followed by its
    count (if that count is more than 1), and so on.
    '''
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [Counter()]
        token = ""
        count = ""
        paren = False
        for c in formula:
            if c == '(':
                if paren:
                    cnt = int(count) if count else 1
                    p = stack.pop()
                    for s in p:
                        stack[-1][s] += p[s] * cnt
                    token = ""
                    count = ""
                    paren = False
                if token:
                    cnt = int(count) if count else 1
                    stack[-1][token] += cnt
                    token = ""
                    count = ""
                stack.append(Counter())
            elif c == ')':
                if paren:
                    c = int(count) if count else 1
                    p = stack.pop()
                    for s in p:
                        stack[-1][s] += p[s] * c
                    token = ""
                    count = ""
                if token:
                    c = int(count) if count else 1
                    stack[-1][token] += c
                    token = ""
                    count = ""
                paren = True
            elif c.isupper():
                if paren:
                    cnt = int(count) if count else 1
                    p = stack.pop()
                    for s in p:
                        stack[-1][s] += p[s] * cnt
                    token = ""
                    count = ""
                    paren = False
                if token:
                    cnt = int(count) if count else 1
                    stack[-1][token] += cnt
                    token = ""
                    count = ""
                token += c
            elif c.isdigit():
                count += c
            else:
                token += c
        if paren:
            c = int(count) if count else 1
            p = stack.pop()
            for s in p:
                stack[-1][s] += p[s] * c
            token = ""
            count = ""
            paren = False
        if token:
            c = int(count) if count else 1
            stack[-1][token] += c
            token = ""
            count = ""
        answer = ""
        for s in sorted(stack[-1].keys()):
            answer += s
            if stack[-1][s] > 1:
                answer += str(stack[-1][s])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "H2O"
        o = "H2O"
        self.assertEqual(s.countOfAtoms(i), o)

    def test_two(self):
        s = Solution()
        i = "Mg(OH)2"
        o = "H2MgO2"
        self.assertEqual(s.countOfAtoms(i), o)

    def test_three(self):
        s = Solution()
        i = "K4(ON(SO3)2)2"
        o = "K4N2O14S4"
        self.assertEqual(s.countOfAtoms(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)