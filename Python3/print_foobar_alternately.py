# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from threading import Lock, Semaphore
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# getting error on Leetcode
# Thread 'foo' threw an exception: '_thread.lock' object is not callable
# seems to be something wrong with pickle... which is something LeetCode is trying to do?
class FooBar_Lock:
    def __init__(self, n):
        self.n = n
        self.f = Lock()
        self.b = Lock()
        self.b.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.f.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.b.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()

class FooBar_Semaphore:
    def __init__(self, n):
        self.n = n
        self.f = Semaphore(0)
        self.b = Semaphore(1)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.b.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.f.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.f.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.b.release()

class UnitTesting(unittest.TestCase):
    '''
    Tested online because threading
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)