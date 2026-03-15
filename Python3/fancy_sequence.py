# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

MODULO = 10**9+7

def moduloAddition(a:int, b:int) -> int:
    return ((a % MODULO) + (b % MODULO)) % MODULO

def moduloMultiplication(a:int, b:int) -> int:
    return ((a % MODULO) * (b % MODULO)) % MODULO

'''
Write an API that generates fancy sequences using the append, addAll, and
multAll operations.

Implement the Fancy class:
'''
class Fancy_TLE:
    '''
    Initializes the object with an empty sequence.
    '''
    def __init__(self):
        # (appended value, operation index when appended)
        self.sequence:List[List[int,int]] = list()
        # (value of operation, type of operation)
        self.operation:List[List[int,int]] = list()

    '''
    Appends an integer val to the end of the sequence.
    '''
    def append(self, val: int) -> None:
        self.sequence.append([val, len(self.operation)])

    '''
    Increments all existing values in the sequence by an integer int.
    '''
    def addAll(self, inc: int) -> None:
        # if self.operation and self.operation[-1][-1] == 0:
        #     sel
        # else:
        self.operation.append([inc,0])

    '''
    Multiplies all existing values in the sequence by an integer m.
    '''
    def multAll(self, m: int) -> None:
        # if self.operation and self.operation[-1][-1] == 1:
        #     pass
        # else:
        self.operation.append([m,1])

    '''
    Gets the current value at index idx (0-indexed) of the sequence modulo
    10^9 + 7. If the index is greater or equal than the length of the sequence,
    return -1.
    '''
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        answer,operationIndex = self.sequence[idx]
        for opVal, opType in self.operation[operationIndex:]:
            if opType == 0:
                answer = moduloAddition(answer, opVal)
            elif opType == 1:
                answer = moduloMultiplication(answer, opVal)
        self.sequence[idx] = [answer,len(self.operation)]
        return answer

# based on editorial
# https://leetcode.com/problems/fancy-sequence/editorial/?envType=daily-question&envId=2026-03-15
# can represent the multiplication and addition at any step by ax+b
# b is addition
# a is multiple (but also multiples b when updated)
# it is possible to use past state and current state to get required mult and add
# this gets messy due to large number and require modulo inverse to calculate
# - lot of fancy algorithms needed accurately derive this
class Fancy:
    def __init__(self):
        self.sequence = list()
        self.additions = [0]
        self.multiplications = [1]

    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.additions.append(self.additions[-1])
        self.multiplications.append(self.multiplications[-1])

    def addAll(self, inc: int) -> None:
        self.additions[-1] = moduloAddition(self.additions[-1], inc)

    def multAll(self, m: int) -> None:
        self.multiplications[-1] = moduloMultiplication(self.multiplications[-1], m)
        self.additions[-1] = moduloMultiplication(self.additions[-1], m)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        # use modulo inverse to calculate (other steps too)
        mul = pow(self.multiplications[idx], MODULO - 2, MODULO) * self.multiplications[-1]
        add = self.additions[-1] - self.additions[idx] * mul
        return moduloAddition(moduloMultiplication(mul, self.sequence[idx]), add)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Fancy()
        s.append(2)
        s.addAll(3)
        s.append(7)
        s.multAll(2)
        self.assertEqual(s.getIndex(0), 10)
        s.addAll(3)
        s.append(10)
        s.multAll(2)
        self.assertEqual(s.getIndex(0), 26)
        self.assertEqual(s.getIndex(1), 34)
        self.assertEqual(s.getIndex(2), 20)

if __name__ == '__main__':
    unittest.main(verbosity=2)