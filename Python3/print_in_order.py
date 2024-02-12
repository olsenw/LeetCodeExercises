# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from threading import Barrier
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Suppose there is a class Foo.

public class Foo {
  public void first() {print("first");}
  public void second() {print("second");}
  public void third() {print("third);}
}

The same instance of Foo will be passed to three
different threads. Thread A will call first, thread B will call second(), and
thread C will call third(). Design a mechanism and modify the program to ensure
that second() is executed after first(), and third() is executed after second().

Note:
It is unknown how the threads will be scheduled in the operating system, even
though the numbers numbers in the input seem to imply the ordering. The input
format is to ensure test comprehensiveness.
'''
class Foo:
    def __init__(self):
        self.b = Barrier(3)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.b.wait()
        self.b.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.b.wait()
        printSecond()
        self.b.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.b.wait()
        self.b.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

class UnitTesting(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)