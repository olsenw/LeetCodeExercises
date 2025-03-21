# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n different recipes. Given a string array recipes and a 2D string
    array ingredients. The ith recipe has the name recipes[i] and it can only be
    created if all the required ingredients from ingredients[i] are present. A
    recipe can also be an ingredient for other recipes, ie, ingredients[i] may
    contain a string that is in recipes.

    Also given is a string array supplies containing all the ingredients that
    are initially present in an infinite supply.

    Return a list of all the recipes that can be created. The answer may be
    returned in any order.

    Note that two recipes may contain each other in their ingredients.
    '''
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # "ingredient" : [indegree, ["used in recipe"]]
        graph = {s:[0,[]] for s in supplies}
        for i in range(len(recipes)):
            if recipes[i] not in graph:
                graph[recipes[i]] = [len(ingredients[i]),[]]
            else:
                graph[recipes[i]][0] = len(ingredients[i])
            for ingredient in ingredients[i]:
                if ingredient in graph:
                    graph[ingredient][1].append(recipes[i])
                else:
                    graph[ingredient] = [1000,[recipes[i]]]
        answer = set()
        def dfs(ingredient:str):
            if graph[ingredient][0] != 0:
                return
            answer.add(ingredient)
            for recipe in graph[ingredient][1]:
                graph[recipe][0] -= 1
                if graph[recipe][0] == 0:
                    dfs(recipe)
            return
        for i in supplies:
            dfs(i)
        answer.difference_update(supplies)
        return list(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["bread"]
        j = [["yeast","flour"]]
        k = ["yeast","flour","corn"]
        o = ["bread"]
        self.assertEqual(s.findAllRecipes(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ["bread","sandwich"]
        j = [["yeast","flour"],["bread","meat"]]
        k = ["yeast","flour","meat"]
        o = ["bread","sandwich"]
        self.assertEqual(s.findAllRecipes(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = ["bread","sandwich","burger"]
        j = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
        k = ["yeast","flour","meat"]
        o = ["bread","sandwich","burger"]
        self.assertEqual(s.findAllRecipes(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)