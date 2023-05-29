# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a parking system for a parking lot. The parking log has three kinds of
parking spaces: big, medium, and small, with a fixed number of slots for each
size.

Implement the ParkingSystem class.
'''
class ParkingSystem:
    '''
    Initializes object of the ParkingSystem class. The number of slots for each
    parking space are given as part of the constructor.
    '''
    def __init__(self, big: int, medium: int, small: int):
        self.spots = [0,big,medium,small]

    '''
    Checks whether there is a parking space of carType for the car that wants to
    get into the parking lot. carType can be of three kinds: big, medium, or
    small, which are represented by 1, 2, and 3 respectively. A car can only
    park in a parking space of its carType. If there is no space available,
    return false, else park the car in that size space and return.
    '''
    def addCar(self, carType: int) -> bool:
        self.spots[carType] -= 1
        return self.spots[carType] >= 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = ParkingSystem(1,1,0)
        self.assertEqual(s.addCar(1), True)
        self.assertEqual(s.addCar(2), True)
        self.assertEqual(s.addCar(3), False)
        self.assertEqual(s.addCar(1), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)