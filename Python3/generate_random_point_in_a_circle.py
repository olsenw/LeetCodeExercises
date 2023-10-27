# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import random
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution_fails:
    '''
    Given the radius and the position of the center of a circle, implement the
    function randPoint which generates a uniform random point inside the circle.

    Implement the solution class:
    * Solution(double radius, double x_center, double y_center) initializes the
      object with the radius of the circle radius and the position of the center
      (x_center, y_center).
    * randPoint() returns a random point inside the circle. A point on the
      circumference of the circle is considered to be in the circle. The answer
      is returned as an array [x,y].
    '''
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        a = random.random() * 2 * math.pi
        # r = random.random() * self.radius
        # Inverse transform sampling
        # without this the points on circles of different radius will not have
        # uniform distribution. use of sqrt solves this
        # needed help of post by DBabichev to understand need for sqrt
        # https://leetcode.com/problems/generate-random-point-in-a-circle/solutions/1113679/python-polar-coordinates-explained-with-diagrams-and-math/
        r = math.sqrt(random.random()) * self.radius
        c = math.cos(a)
        s = math.sin(a)
        x = c * r + self.x
        y = s * r + self.y
        return [x,y]

class UnitTesting(unittest.TestCase):
    # tested online
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)