# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Under the grammar given below, strings can represent a set of lowercase
    words. Let R(expr) denote the set of words the expression represents.

    The grammar can best be understood through simple examples:
    * Single letters represent a singleton set containing the word.
      * R("a") = {"a"}
      * R("w") = {"w"}
    * When there is a comma-delimited list of two or more expressions or have
      expressions, take the union of possibilities.
      * R("{a,b,c}") = {"a", "b", "c"}
      * R("{{a,b},{b,c}}") = {"a", "b", "c"}
    * When two expressions are concatenated take the set of possible
      concatenations between two words where the first word comes from the first
      expression and the second word comes from the second expression.
      * R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
      * R("a{b,c}{d,e}f{g,h}) = {"abdfg", "abdfh", "abefg", "abefh", "acdfg",
        "acdfh", "acefg", "acefh"}
    
    Formally, the three rules of the grammar:
    * For every lowercase letter x, R(x) = {x}.
    * For expressions e1, e2, ..., ek with k >= 2, R({e1, e2, ...}) =
      R(e1) U R(...)
    * For expressions e1 and e2, R(e1 + e2) = {a + b for (a,b) in R(ei) x R(e2)},
      where + denotes concatenation, and x denote the cartesian product.
    
    Given an expression representing a set of words under the given grammar,
    return the sorted list of words that the expression represents.
    '''
    def braceExpansionII_fails(self, expression: str) -> list[str]:
        class LeafNode:
            def __init__(self):
                self.value = ""
            def __repr__(self):
                return f'"{self.value}"'
            def append(self, s:str):
                self.value += s
            def isEmpty(self) -> bool:
                return self.value == ""
            def answer(self) -> Set:
                return {self.value}
        class TreeNode:
            def __init__(self):
                self.children = [LeafNode()]
            def __repr__(self):
                s = ",".join(repr(c) for c in self.children)
                return f'({s})'
            def addNode(self) -> 'TreeNode':
                self.truncate()
                self.children.append(TreeNode())
                return self.children[-1]
            def addLeaf(self) -> LeafNode:
                self.children.append(LeafNode())
            def appendLeaf(self, s:str):
                self.children[-1].append(s)
            def truncate(self):
                if type(self.children[-1]) is LeafNode and self.children[-1].isEmpty():
                    self.children.pop()
            def answer(self) -> Set:
                a = [c.answer() for c in self.children]
                r = {""}
                for i in a:
                    for j in i:
                        b = set()
                        for k in r:
                            b.add(j + k)
                        r = b
                return r
        stack = [TreeNode()]
        for i in expression:
            if i == '{':
                stack.append(stack[-1].addNode())
            elif i == '}':
                stack[-1].truncate()
                stack.pop()
                stack[-1].addLeaf()
            elif i == ',':
                stack[-1].addLeaf()
            else:
                stack[-1].appendLeaf(i)
        stack[-1].truncate()
        return sorted(stack[-1].answer())

    # based on Leetcode editorial
    # https://leetcode.com/problems/brace-expansion-ii/editorial/?envType=daily-question&envId=2026-09-25
    # basics of language parsing
    def braceExpansionII(self, expression: str) -> list[str]:
        index = 0
        n = len(expression)
        def isLetter(c:str) -> bool:
            return "a" <= c <= "z"
        # Recursive descent parser
        # expr -> term | term, expr
        def expr() -> set:
            nonlocal index
            answer = set()
            while True:
                # union the answer with the result of term
                answer |= term()
                # only continue if comma is matched
                if index < n and expression[index] == ',':
                    index += 1
                    continue
                break
            return answer
        # concatenation
        # term -> item | item term
        def term() -> set:
            nonlocal index
            answer = {""}
            while index < n and (expression[index] == '{' or isLetter(expression[index])):
                sub = item()
                temp = set()
                for left in answer:
                    for right in sub:
                        temp.add(left + right)
                answer = temp
            return answer
        # single letters or sub expressions
        # item -> item | { expr }
        def item() -> set:
            nonlocal index
            answer = set()
            if expression[index] == '{':
                index += 1
                answer = expr()
            else:
                answer = {expression[index]}
            index += 1
            return answer
        # get sorted list of answer
        return sorted(expr())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "{a,b}{c,{d,e}}"
        o = ["ac","ad","ae","bc","bd","be"]
        self.assertEqual(s.braceExpansionII(i), o)

    def test_two(self):
        s = Solution()
        i = "{{a,z},a{b,c},{ab,z}}"
        o = ["a","ab","ac","z"]
        self.assertEqual(s.braceExpansionII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)