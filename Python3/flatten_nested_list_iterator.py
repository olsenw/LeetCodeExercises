# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class NestedInteger:
    def __init__(self, i=None, l=None):
        self.i = i
        self.l = l

    def isInteger(self) -> bool:
        return self.i != None

    def getInteger(self) -> int:
        return self.i

    def getList(self):
        return self.l

'''
Given a nested list of integers nestedList. Each element is either an
integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.
'''
# does not handle the case of an empty list
# tried to be too smart...
class NestedIterator_stack_fails:
    def __init__(self, nestedList: [NestedInteger]):
        self.s = [iter(nestedList)]
        self.l = len(nestedList)
        n = nestedList[0]
        while not n.isInteger():
            n = n.getList()
            self.s.append(iter(n))
            self.l += len(n) - 1
        pass

    def next(self) -> int:
        try:
            n = next(self.s[-1])
            if n.isInteger():
                self.l -= 1
                return n.getInteger()
            else:
                n = n.getList()
                self.s.append(iter(n))
                self.l += len(n) - 1
                return self.next()
        except:
            self.s.pop()
            return self.next()

    def hasNext(self) -> bool:
        return self.l > 0

# brute force flattens nestedList into a list and iterates over that
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.i = 0
        self.s = []
        def cycle(nlist):
            for n in nlist:
                if n.isInteger():
                    self.s.append(n.getInteger())
                else:
                    cycle(n.getList())
        cycle(nestedList)


    def next(self) -> int:
        self.i += 1
        return self.s[self.i - 1]

    def hasNext(self) -> bool:
         return self.i < len(self.s)

class UnitTesting(unittest.TestCase):
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())

    '''
    The implementation of NestedInteger is unknown... so these tests may
    not reflect leetcode correctly.
    '''

    def test_one(self):
        s = NestedIterator([
            NestedInteger(None, [NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger(None, [NestedInteger(1), NestedInteger(1)])
        ])
        i = []
        while s.hasNext():
            i.append(s.next())
        o = [1,1,2,1,1]
        self.assertEqual(i, o)

    def test_two(self):
        s = NestedIterator([
            NestedInteger(1),
            NestedInteger(None, [NestedInteger(4), NestedInteger(None, [NestedInteger(6)])]),
        ])
        i = []
        while s.hasNext():
            i.append(s.next())
        o = [1,4,6]
        self.assertEqual(i, o)

    def test_three(self):
        s = NestedIterator([
            NestedInteger(None, []),
        ])
        i = []
        while s.hasNext():
            i.append(s.next())
        o = []
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)