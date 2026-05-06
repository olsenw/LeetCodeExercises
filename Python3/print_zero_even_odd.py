# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from threading import Barrier
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There is a function printNumber that can be called with an integer parameter and
prints it to the console.

Given an instance of the class ZeroEvenOdd that has three functions: zero, even,
and odd. The same instance of ZeroEvenOdd will be passed to three different
threads:
* Thread A: calls zero() that should only output 0's.
* Thread B: calls even() that should only output even numbers.
* Thread C: calls odd() that should only output odd numbers.

Modify the ZeroEvenOdd class to output the series "010203040506..." where the
length of the series must be 2n.

Implement the ZeroEvenOdd class:
'''
class ZeroEvenOdd:
    '''
    Initializes the object with the number n that represents the number that
    should be printed.
    '''
    def __init__(self, n):
        self.n = n
        self.x = 0
        self.b = Barrier(3)
        
    '''
    Calls printNumber to output one zero.
    '''
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.x < self.n:
            self.b.wait()
            self.x += 1
            printNumber(0)
            self.b.wait()
            # even
            self.b.wait()
            # odd
        pass
        
    '''
    Calls printNumber to output one even number.
    '''
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.x < self.n:
            self.b.wait()
            # printNumber(0)
            self.b.wait()
            # even
            if self.x % 2 == 0:
                printNumber(self.x)
            self.b.wait()
            # odd
        pass
        
    '''
    Calls printNumber to output one odd number.
    '''
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.x < self.n:
            self.b.wait()
            # printNumber(0)
            self.b.wait()
            # even
            self.b.wait()
            # odd
            if self.x % 2 == 1:
                printNumber(self.x)
        pass

class UnitTesting(unittest.TestCase):
    pass
    '''
    Tested online due to multi threaded question.
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)