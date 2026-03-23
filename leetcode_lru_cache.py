##https://leetcode.com/problems/lru-cache/description/
class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        self._usage_heap = []
        self._size = 0

    def get(self, key: int) -> int:
        if key in self._cache:
            [value, usage] = self._cache[key]
            self._cache[key] = [value, usage+1]
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        usage = 0
        #for an existing key, do not overwrite usage
        if key in self._cache:
            usage = self._cache[key][1]
        else:
            if len(self._cache) == self._capacity:
                print ('Invoke eviction')
        self._cache[key] = [value, usage]
        print (self._cache)


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