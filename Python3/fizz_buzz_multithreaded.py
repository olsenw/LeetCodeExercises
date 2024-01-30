# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from threading import Barrier, Lock, Event
from time import sleep
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There are four functions:
* printFizz that prints the word "fizz" to the console,
* printBuzz that prints the word "buzz" to the console,
* printFizzBuzz that prints the word "fizzbuzz" to the console, and
* printNumber that prints a given integer to the console.

Given an instance of the class FizzBuzz that has four functions: fizz, buzz,
fizzbuzz and number. The same instance of FizzBuzz will be passed to four
different threads:
* Thread A: calls fizz() that should output "fizz".
* Thread B: calls Buzz() that should output the word "buzz".
* Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
* Thread D: cass number() that should only output the integers.

Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where
the ith token (1-indexed) if the series is:
* "fizzbuzz" if i is divisible by 3 and 5,
* "fizz" if i is divisible by 3 and not 5,
* "buzz" if i is divisible by 5 and not 3, or
* i if i is not divisible by 3 or 5.

Implement the FizzBuzz class:
'''
class FizzBuzz_Mutex_fails:
    '''
    Initializes the object with the number n that represents the length of the
    sequence that should be printed
    '''
    def __init__(self, n: int):
        self.n = n
        self.c = 1
        self.m = Lock()

    '''
    Calls printFizz to output "fizz".
    '''
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 0 and self.c % 5 == 1:
                    printFizz()
                    self.c += 1

    '''
    Calls printBuzz to output "buzz".
    '''
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 1 and self.c % 5 == 0:
                    printBuzz()
                    self.c += 1
            sleep(0)

    '''
    Calls printFizzBuzz to output "fizzbuzz".
    '''
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 0 and self.c % 5 == 0:
                    printFizzBuzz()
                    self.c += 1

    '''
    Calls printnumber to output the numbers.
    '''
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 1 and self.c % 5 == 1:
                    printNumber(self.c)
                    self.c += 1

class FizzBuzz_Event_fails:
    def __init__(self, n: int):
        self.n = n
        self.c = 1
        self.e = Event()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            self.e.set()
            if self.c % 3 == 0 and self.c % 5 == 1:
                printFizz()
                self.c += 1
                self.e.set()
            self.e.wait()
        self.e.set()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            self.e.set()
            if self.c % 3 == 0 and self.c % 5 == 1:
                printBuzz()
                self.c += 1
                self.e.set()
            self.e.wait()
        self.e.set()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            self.e.set()
            if self.c % 3 == 0 and self.c % 5 == 1:
                printFizzBuzz()
                self.c += 1
                self.e.set()
            self.e.wait()
        self.e.set()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.c <= self.n:
            self.e.set()
            if self.c % 3 == 0 and self.c % 5 == 1:
                printNumber(self.c)
                self.c += 1
                self.e.set()
            self.e.wait()
        self.e.set()

# this fails because the number of times each thread goes through the loop are not the same
class FizzBuzz_Barrier_fails:
    def __init__(self, n: int):
        self.n = n
        self.c = 1
        self.b = Barrier(4)
        self.m = Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 0 and self.c % 5 != 0:
                    printFizz()
                    self.c += 1
            self.b.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 != 0 and self.c % 5 == 0:
                    printBuzz()
                    self.c += 1
            self.b.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 == 0 and self.c % 5 == 0:
                    printFizzBuzz()
                    self.c += 1
            self.b.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.c <= self.n:
            with self.m:
                if self.c % 3 != 0 and self.c % 5 != 0:
                    printNumber(self.c)
                    self.c += 1
            self.b.wait()

# solution by idontknoooo
# https://leetcode.com/problems/fizz-buzz-multithreaded/solutions/2956831/python-3-5-approaches-lock-semaphore-event-condition-explanation/
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n + 1
        self.b = Barrier(4)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(1, self.n):
            if i % 3 == 0 and i % 5:
                printFizz()
            self.b.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(1, self.n):
            if i % 3 and i % 5 == 0:
                printBuzz()
            self.b.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()
            self.b.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            if i % 3 and i % 5:
                printNumber(i)
            self.b.wait()

class UnitTesting(unittest.TestCase):
    # tested online due to threads
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)