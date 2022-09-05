# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    A car travels from a starting position to a destination which is
    target miles east of the starting position.

    There are gas stations along the way. The gas stations are
    represented as an array stations where
    stations[i] = [positions_i, fuel_i] indicates that the ith gas
    stations is position_i miles east of the starting position and has
    fuel_i liters of gas.

    The car starts with an infinite tank of gas, which initially has
    startFuel liters of fuel in it. It uses one liter of gas per one
    mile that it drives. When the car reaches a gas station, it may stop
    and refuel, transferring all the gas from the station into the car.

    Return the minimum number of refueling stops the car must make in
    order to reach its destination. If it cannot reach the destination
    return -1.

    Note that if the car reaches a gas station with zero fuel left, the
    car can still refuel there. If the car reaches the destination with
    zero fuel left, it is still considered to have arrived.
    '''
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # pointed out that can use heap to solve...
        gas = []
        stops = 0
        index = 0
        fuel = startFuel
        print("fuel:", fuel, "stops:", stops, "index:", index)
        while fuel < target:
            while index < len(stations):
                if stations[index][0] <= fuel:
                    heapq.heappush(gas, -stations[index][1])
                else:
                    break
                index += 1
            if not gas:
                return -1
            fuel += -1 * heapq.heappop(gas)
            stops += 1
            # print(len(gas), gas[0], "fuel:", fuel, "stops:", stops, "index:", index) if gas else print("fuel:", fuel, "stops:", stops, "index:", index)
        # return stops if fuel >= target else -1
        return stops

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 1
        k = []
        o = 0
        self.assertEqual(s.minRefuelStops(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 100
        j = 1
        k = [[10,100]]
        o = -1
        self.assertEqual(s.minRefuelStops(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 100
        j = 10
        k = [[10,60],[20,30],[30,30],[60,40]]
        o = 2
        self.assertEqual(s.minRefuelStops(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)