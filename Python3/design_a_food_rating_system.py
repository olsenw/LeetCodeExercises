# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a food rating system that can do the following:
* Modify the rating of a food item listed in the system.
* Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:
'''
class FoodRatings:
    '''
    Initializes the system. The food items are described by foods, cuisines and
    ratings, all of which have a length of n.
    * foods[i] is the name of the ith food.
    * cuisines[i] is the type of cuisine of the ith food.
    * ratings[i] is the initial rating of the ith food.
    '''
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.foods = dict()
        self.ratings = dict()
        for f,c,r in zip(foods, cuisines, ratings):
            heapq.heappush(self.cuisines[c], (-r,f))
            self.foods[f] = c
            self.ratings[f] = -r

    '''
    Changes the rating of the food item with the name food.
    '''
    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = -newRating
        heapq.heappush(self.cuisines[self.foods[food]], (-newRating,food))

    '''
    Returns the name of the food item that has the highest rating for the given
    type of cuisine, if there is a tie, return the item with the
    lexicographically smaller name.
    '''
    def highestRated(self, cuisine: str) -> str:
        while True:
            r,f = self.cuisines[cuisine][0]
            if self.ratings[f] == r:
                return f
            heapq.heappop(self.cuisines[cuisine])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = FoodRatings(
            ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
            ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
            [9, 12, 8, 15, 14, 7]
        )
        self.assertEqual(s.highestRated("korean"), "kimchi")
        self.assertEqual(s.highestRated("japanese"), "ramen")
        s.changeRating("sushi", 16)
        self.assertEqual(s.highestRated("japanese"), "sushi")
        s.changeRating("ramen", 16)
        self.assertEqual(s.highestRated("japanese"), "ramen")

if __name__ == '__main__':
    unittest.main(verbosity=2)