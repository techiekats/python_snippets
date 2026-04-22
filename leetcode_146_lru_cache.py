##https://leetcode.com/problems/lru-cache/description/
class Node:
    def __init__(self, value:int):
        self._value = value
        self._prev = None
        self._next = None
    def getValue (self):
        return self._value
    def getPrev (self):
        return self._prev
    def getNext (self):
        return self._next
    def setPrev (self, x):
        self._prev = x
    def setNext (self, x):
        self._next = x
    def setValue (self, x):
        self._value = x
class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        ##NOTE: these are sentinel nodes. This pattern simplified the myriad of edge cases in doubly linked lists
        ## E.g. of edge cases that would need to be handled:
        #       - How to initialize when both head and tail nodes are the same
        #       - How to delete when cache size = 1
        #       - When cache size is 2; and the tail becomes new head...
        self._head = Node(-1)
        self._tail = Node(-1)
        self._head.setNext(self._tail)
        self._tail.setNext(self._head)
        self._head.setPrev(self._tail)
        self._tail.setNext(self._head)

    ##This assumes the node already exists in the doubly linked list
    def resetHeadTo(self, node:Node):       
        node.setNext(self._head.getNext())
        node.setPrev(self._head)
        self._head.getNext().setPrev(node)
        self._head.setNext(node) ## The node effectively becomes the new head
    
    def performByPass (self, node:Node):
        node.getPrev().setNext(node.getNext())
        node.getNext().setPrev(node.getPrev())
        node.setNext(None)
        node.setPrev(None)

    def get(self, key: int) -> int:
        value = -1
        if key in self._cache:
            [value, node] = self._cache[key]
            self.performByPass(node)
            self.resetHeadTo(node)
        return value

    def put(self, key: int, value: int) -> None:
        node = None

        if key not in self._cache:
            if len(self._cache) == self._capacity:
                # cache eviction
                eviction_key = self._tail.getPrev().getValue()
                del self._cache[eviction_key]
                new_tail = self._tail.getPrev().getPrev()
                new_tail.setNext(self._tail)
                self._tail.setPrev(new_tail)
            node = Node(key)
        else:
            node = self._cache[key][1]
            self.performByPass(node)
            
        self._cache[key] = [value, node]
        self.resetHeadTo(node)


lRUCache = LRUCache(2)
lRUCache.put(2,1)
lRUCache.put(1,1)
lRUCache.put(2,3)
lRUCache.put(4,1)
assert lRUCache.get(1) == -1
assert lRUCache.get(2) == 3

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1 = 1}
lRUCache.put(2, 2) # cache is {1 = 1, 2 = 2}
assert lRUCache.get(1) == 1 # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
assert lRUCache.get(2) == -1 # returns - 1(not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
assert lRUCache.get(1) == -1 # return -1(not found)
assert lRUCache.get(3) == 3 # return 3
assert lRUCache.get(4) == 4# return 4

lRUCache = LRUCache(1)
assert lRUCache.get(3) == -1
lRUCache.put(3, 4)
assert lRUCache.get (3) == 4
lRUCache.put(3,6)
assert lRUCache.get(3) == 6
lRUCache.put(5,7)
assert lRUCache.get(3) == -1
assert lRUCache.get(5) == 7

lRUCache = LRUCache(5)
lRUCache.put(1,1)
lRUCache.put(2,2)
lRUCache.put(3,3)
lRUCache.put(4,4)
lRUCache.put(5,5)
for i in range (1,6):
    assert lRUCache.get(i) == i

lRUCache.put(6,6)
assert lRUCache.get(1) == -1
assert lRUCache.get(5) == 5