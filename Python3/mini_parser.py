# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       pass

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       pass

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       pass

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       pass

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       pass

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       pass

class Solution:
    '''
    Given a string s represents the serialization of a nested list, implement a
    parser to deserialize it and return the deserialized NestedInteger.

    Each element is either an integer or a list whose elements may also be
    integers or other lists
    '''
    def deserialize_fails(self, s: str) -> NestedInteger:
        def parse(i:int) -> Tuple[NestedInteger,int]:
            if s[i] != '[':
                curr = ""
                while i < len(s):
                    if s[i] not in "[],":
                        curr += s[i]
                        i += 1
                    else:
                        return (NestedInteger(int(curr)),i)
            answer = NestedInteger()
            curr = ""
            while i < len(s):
                c = s[i]
                if c == '[':
                    n,i = parse(i)
                    answer.add(n)
                elif c == ']':
                    return (answer, i+1)
                elif c == ',':
                    answer.add(NestedInteger(int(curr)))
                    curr = ""
                else:
                    curr += c
        return parse(0)[0]

    def deserialize(self, s: str) -> NestedInteger:
        def parseInteger(i:int) -> Tuple[NestedInteger, int]:
            curr = ""
            while i < len(s):
                if s[i] in "[,]":
                    return (NestedInteger(int(curr)), i)
                curr += s[i]
                i += 1
            return (NestedInteger(int(curr)), i)
        def parseList(i: int) -> Tuple[NestedInteger, int]:
            answer = NestedInteger()
            i += 1
            while i < len(s):
                if s[i] == ']':
                    return (answer, i+1)
                elif s[i] == '[':
                    a,i = parseList(i)
                    answer.add(a)
                elif s[i] == ',':
                    i += 1
                else:
                    a,i = parseInteger(i)
                    answer.add(a)
            return answer
        if s[0] == '[':
            return parseList(0)[0]
        return parseInteger(0)[0]

class UnitTesting(unittest.TestCase):
    '''
    Tested online due to not having implementation of NestedInteger Class
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)