# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Design an algorithm that collects daily price quotes for some stock and returns
the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backward) for which the stock
price was less than or equal to today's price.

Implement the StockSpanner class.
'''
# O(n^2) time
class StockSpanner_brute:
    # Initializes the object of the class.
    def __init__(self):
        self.s = []

    # Returns the span of the stock's price given that today's price is price.
    def next(self, price: int) -> int:
        self.s.append(price)
        span = 1
        for n in self.s[-2::-1]:
            if self.s[-1] < n:
                break
            span += 1
        return span

class StockSpanner_monotonic:
    # Initializes the object of the class.
    def __init__(self):
        self.s = []

    # Returns the span of the stock's price given that today's price is price.
    def next(self, price: int) -> int:
        removed = 0
        while self.s and self.s[-1][0] <= price:
            removed += self.s.pop()[1]
        self.s.append((price, removed + 1))
        return self.s[-1][1]

class StockSpanner_monotonic_alt:
    # Initializes the object of the class.
    def __init__(self):
        self.p = []
        self.s = []

    # Returns the span of the stock's price given that today's price is price.
    def next(self, price: int) -> int:
        removed = 0
        while self.p and self.p[-1] <= price:
            self.p.pop()
            removed += self.s.pop()
        self.p.append(price)
        self.s.append(removed + 1)
        return self.s[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = StockSpanner()
        inputs = [100, 80, 60, 70, 60, 75, 85]
        outputs = [1, 1, 1, 2, 1, 4, 6]
        for i,o in zip(inputs, outputs):
            self.assertEqual(s.next(i), o)

    def test_two(self):
        s = StockSpanner()
        inputs = [28,14,28,35,46,53,66,80,87,88]
        outputs = [1,1,3,4,5,6,7,8,9,10]
        for i,o in zip(inputs, outputs):
            self.assertEqual(s.next(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)