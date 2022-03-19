# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import defaultdict, Counter
class FreqStack:
    '''
    Design a stack-like data structure to push elements to the stack and
    pop the most frequent element from the stack.

    Implement the FreqStack class:
    * FreqStack() constructs an empty frequency stack.
    * void push(int val) pushes an integer val onto the top of the
      stack.
    * int pop() removes and returns the most frequent element in the
      stack.
      # if there is a tie for the most frequent element, the element
        closest to the stack's top is removed and returned.
    '''
    # based on solution by lee215
    # https://leetcode.com/problems/maximum-frequency-stack/discuss/163410/C%2B%2BJavaPython-O(1)
    # basically the idea of storing the stack of numbers with given
    # frequency instead of my lookup nonsense
    def __init__(self):
        self.freq = Counter()
        self.stack = defaultdict(list)
        self.smax = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.smax = max(self.freq[val], self.smax)
        self.stack[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self.smax].pop()
        if not self.stack[self.smax]:
            self.smax -= 1
        self.freq[val] -= 1
        return val

# time limit exceeded passes 31/37 test cases
class FreqStack_Time_Exceeded:
    def __init__(self):
        self.index = 0
        self.order = defaultdict(list)
        self.freq = defaultdict(set)
        self.fmax = 0
        pass

    def push(self, val: int) -> None:
        if len(self.order[val]):
            l = len(self.order[val])
            self.freq[l].remove(val)
            self.order[val].append(self.index)
            self.freq[l + 1].add(val)
            self.index += 1
            self.fmax = max(l + 1, self.fmax)
        else:
            self.order[val].append(self.index)
            self.freq[1].add(val)
            self.index += 1
            self.fmax = max(1, self.fmax)

    def pop(self) -> int:
        _, val = max((self.order[v][-1],v) for v in self.freq[self.fmax])
        # pop index from order
        self.order[val].pop()
        # remove value from freq[fmax]
        self.freq[self.fmax].remove(val)
        # add value to freq[fmax] (the updated fmax) if fmax > 0
        if self.fmax - 1 > 0 and len(self.order[val]) > 0:
            self.freq[self.fmax - 1].add(val)
        # decrement fmax
        if not len(self.freq[self.fmax]):
            self.fmax -= 1
        return val

class UnitTesting(unittest.TestCase):
    def test_one(self):
        fs = FreqStack()
        fs.push(5)
        fs.push(7)
        fs.push(5)
        fs.push(7)
        fs.push(4)
        fs.push(5)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 7)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 4)

    def test_two(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)