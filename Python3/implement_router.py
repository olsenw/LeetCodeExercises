# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design a data structure that can efficiently manage data packets in a network
router. Each data packet consists of the following attributes:
* source: A unique identifier for the machine that generated the packet.
* destination: A unique identifier for the target machine.
* timestamp: The time at which the packet arrived at the router.

Implement the Router class:
'''
class Router_tle:
    '''
    Initializes the Router object with a fixed memory limit.
    * memoryLimit is the maximum number of packets the router can store at any
      given time
    * If adding a new packet would exceed this limit, the oldest packet must be
      removed to free up space.
    '''
    def __init__(self, memoryLimit: int):
        self.fifo = deque([])
        self.size = memoryLimit
        self.packets = set()

    '''
    Adds a packet with the given attributes to the router.
    * A packet is considered a duplicate if another packet with the same source,
      destination, and timestamp already exists in the router.
    * Return true if the packet is successfully added (ie, it is not a 
      duplicate); otherwise return false.
    
    Note that queries for addPacket will be made in increasing order of
    timestamp.
    '''
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (timestamp, destination, source)
        if packet in self.packets:
            return False
        if len(self.fifo) == self.size:
            self.fifo.popleft()
        self.fifo.append(packet)
        self.packets.add(packet)
        return True

    '''
    Forwards the next packet in FIFO (First In First Out) order.
    * Remove the packet from storage.
    * Return the packet as an array [source, destination, timestamp].
    * If there are no packets to forward, return an empty array.
    '''
    def forwardPacket(self) -> List[int]:
        if len(self.fifo) == 0:
            return []
        packet = self.fifo.popleft()
        self.packets.remove(packet)
        timestamp, destination, source = packet
        return [source, destination, timestamp]

    '''
    Returns the number of packets currently stored in the router (ie, not yet
    forwarded) that have the specified destination and have timestamps in the
    inclusive range (startTime, endTime)
    '''
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.fifo, startTime, key=lambda x:x[0])
        right = bisect.bisect(self.fifo, endTime, key=lambda x:x[0])
        return sum(self.fifo[i][1] == destination for i in range(left, right))

class Router:

    def __init__(self, memoryLimit: int):
        self.destinations = defaultdict(deque)
        self.packets = set()
        self.fifo = deque()
        self.size = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (timestamp, destination, source)
        if packet in self.packets:
            return False
        if len(self.fifo) == self.size:
            p = self.fifo.popleft()
            self.packets.remove(p)
            self.destinations[p[1]].popleft()
        self.fifo.append(packet)
        self.packets.add(packet)
        self.destinations[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.fifo) == 0:
            return []
        packet = self.fifo.popleft()
        self.packets.remove(packet)
        self.destinations[packet[1]].popleft()
        return [packet[2], packet[1], packet[0]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.destinations[destination], startTime)
        right = bisect.bisect(self.destinations[destination], endTime)
        return right - left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Router(3)
        self.assertEqual(s.addPacket(*[1,4,90]), True)
        self.assertEqual(s.addPacket(*[2,5,90]), True)
        self.assertEqual(s.addPacket(*[1,4,90]), False)
        self.assertEqual(s.addPacket(*[3,5,95]), True)
        self.assertEqual(s.addPacket(*[4,5,105]), True)
        self.assertEqual(s.forwardPacket(), [2,5,90])
        self.assertEqual(s.addPacket(*[5,2,110]), True)
        self.assertEqual(s.getCount(*[5,100,110]), 1)

    def test_two(self):
        s = Router(2)
        self.assertEqual(s.addPacket(*[7,4,90]), True)
        self.assertEqual(s.forwardPacket(), [7,4,90])
        self.assertEqual(s.forwardPacket(), [])

    def test_three(self):
        s = Router(2)
        self.assertEqual(s.addPacket(*[2,1,5]), True)
        self.assertEqual(s.addPacket(*[2,1,6]), True)
        self.assertEqual(s.getCount(*[1,3,6]), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)