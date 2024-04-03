# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        self.dead = False
    def add(self, node) -> None:
        self.children.append(node)
    def kill(self) -> None:
        self.dead = True
    def inheritance(self) -> List[str]:
        l = []
        if not self.dead:
            l.append(self.name)
        for child in self.children:
            l.extend(child.inheritance())
        return l

'''
A kingdom consists of a king, his children, his grandchildren, and so on. Every
once in a while, someone in the family dies or a child is born.

The kingdom has a well-defined order of inheritance that consists of the king as
the first member. Define the recursive function Successor(x, curOrder), which
given a person x and the inheritance order so far, returns who should be the
next person after x in the order of inheritance.

Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder

Very long example on how this works.
'''
class ThroneInheritance:
    '''
    Initializes an object of the ThroneInheritance class. The name of the king
    is given as part of the constructor.
    '''
    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.nodes = {kingName:self.king}

    '''
    Indicates that parentName gave birth to childName.
    '''
    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.nodes[parentName].add(child)
        self.nodes[childName] = child

    '''
    Indicates the death of name. The death of the person doesn't affect the
    Successor function nor the current inheritance order. Treat it as marking
    the person dead.
    '''
    def death(self, name: str) -> None:
        self.nodes[name].kill()

    '''
    Returns a list representing the current order of inheritance excluding dead
    people.
    '''
    def getInheritanceOrder(self) -> List[str]:
        return self.king.inheritance()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = ThroneInheritance("king")
        s.birth("king", "andy")
        s.birth("king", "bob")
        s.birth("king", "catherine")
        s.birth("andy", "matthew")
        s.birth("bob", "alex")
        s.birth("bob", "asha")
        self.assertEqual(s.getInheritanceOrder(), ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"])
        s.death("bob")
        self.assertEqual(s.getInheritanceOrder(), ["king", "andy", "matthew", "alex", "asha", "catherine"])

if __name__ == '__main__':
    unittest.main(verbosity=2)