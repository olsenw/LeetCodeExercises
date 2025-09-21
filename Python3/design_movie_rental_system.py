# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedSet

'''
There is a movie renting company consisting of n shops. Implement a renting
system that supports searching for, booking, and returning movies. The system
should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where
entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie
moviei at shop shopi with a rental price of pricei. Each shop carries at most
one copy of a movie moviei.

the system should support the following functions:
* Search: Finds the cheapest 5 shops that have an unrented copy of a given
  movie. The shops should be sorted by price in ascending order, and in case of
  a tie, the one with the smaller shopi should appear first. If there are less
  than 5 matching shops, then all of them should be returned. If no shop has an
  unrented copy, then an empty list should be returned.
* Rent: Rents an unrented copy of a given movie from a given shop.
* Drop: Drops off a previously rented copy of a given movie at a given shop.
* Report: Returns the cheapest 5 rented movies (possibly of the same movie ID)
  as a 2D list res where res[j] = [shopj, moviej] describes that the jth
  cheapest rented movie moviej was rented from the shop shopj. The movies in res
  should be sorted by price in ascending order, and in case of a tie, the one
  with the smaller shopj should appear first. If there are fewer than 5 rented
  movies, then all of them should be returned. If no movies are currently being
  rented, then an empty list should be returned.

Implement the MovieRentingSystem class:

Note: The test cases will be generated such that rent will only be called if the
shop has an unrented copy of the movie, and drop will only be called if the shop
had previously rented out the movie.
'''
class MovieRentingSystem_tle:
    '''
    Initializes the MovieRentingSystem object with n shops and the movies in
    entries.
    '''
    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = dict()
        self.rented = SortedSet()
        self.movies = SortedSet()
        for shop, movie, price in entries:
            self.prices[(shop,movie)] = price
            self.movies.add((price,shop,movie))
        return

    '''
    Returns a list of shops that have an unrented copy of the given movie as
    described above.
    '''
    def search(self, movie: int) -> List[int]:
        answer = []
        for p,s,m in self.movies:
            if m != movie:
                continue
            answer.append(s)
            if len(answer) == 5:
                break
        return answer

    '''
    Rents the given movie from the given shop.
    '''
    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.movies.remove((price,shop,movie))
        self.rented.add((price,shop,movie))
        return

    '''
    Drops off a previously rented movie at the given shop.
    '''
    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.movies.add((price,shop,movie))
        self.rented.remove((price,shop,movie))
        return

    '''
    Returns a list of cheapest rented movies as described above.
    '''
    def report(self) -> List[List[int]]:
        answer = []
        for p,s,m in self.rented:
            answer.append([s,m])
            if len(answer) == 5:
                break
        return answer

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = dict()
        self.rented = SortedSet()
        self.movies = defaultdict(SortedSet)
        for shop, movie, price in entries:
            self.prices[(shop,movie)] = price
            self.movies[movie].add((price,shop))
        return

    def search(self, movie: int) -> List[int]:
        answer = []
        for price,shop in self.movies[movie]:
            answer.append(shop)
            if len(answer) == 5:
                break
        return answer

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.movies[movie].remove((price,shop))
        self.rented.add((price,shop,movie))
        return

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop,movie)]
        self.rented.remove((price,shop,movie))
        self.movies[movie].add((price,shop))
        return

    def report(self) -> List[List[int]]:
        answer = []
        for price,shop,movie in self.rented:
            answer.append([shop,movie])
            if len(answer) == 5:
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = MovieRentingSystem(*[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]])
        self.assertEqual(s.search(1), [1,0,2])
        s.rent(0,1)
        s.rent(1,2)
        self.assertEqual(s.report(), [[0,1], [1,2]])
        s.drop(1,2)
        self.assertEqual(s.search(2), [0,1])

if __name__ == '__main__':
    unittest.main(verbosity=2)