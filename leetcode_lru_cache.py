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
        self._head = None
        self._tail = None
        self._size = 0

    def get(self, key: int) -> int:
        value = -1
        if key in self._cache:
            [value, node] = self._cache[key]
            if node is None:
                node = Node(key)
                if self._head is None and self._tail is None:
                    self._head = self._tail = node
                    node.setPrev(node)
                    node.setNext(node)
                else:
                    self._head.setPrev (node)
                    self._tail.setNext (node)
                    node.setPrev (self._tail)
                    node.setNext (self._head)
                    self._head = node
            else:
                if node == self._tail:
                    self._head = self._tail
                    self._tail = self._tail.getPrev()
                else:
                    ##if node is head, do nothing
                    if node != self._head:
                        node.getPrev().setNext(node.getNext())
                        node.getNext().setPrev(node.getPrev())
                        node.setNext(self._head.getNext())
                        node.setPrev(self._head.getPrev())
                        self._head = node
        return value

    def put(self, key: int, value: int) -> None:
        value_node = None
        if key not in self._cache:
            if len(self._cache) == self._capacity:
                # cache eviction
                del self._cache[self._tail.getValue()]
                node = self._tail.getPrev()
                node.setNext(self._head)
                self._tail = node
            ##new key now becomes head
            value_node = Node(key)

        else: ##If key is already in cache, cache is already within capacity
            value_node = self._cache[key][1]
            prev = value_node.getPrev()
            next = value_node.getNext()
            if prev is not None:
                prev.setNext(next)
            if next is not None:
                next.setPrev(prev)
        ##inserting and updating make the key the most recent item
        self._cache[key] = [value, value_node]
        value_node.setPrev(self._tail)
        value_node.setNext(self._head)
        if self._head is not None:
            self._head.setPrev(value_node)
        if self._tail is not None:
            self._tail.setNext(value_node)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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