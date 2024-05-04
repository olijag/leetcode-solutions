# https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # If key is not present in the cache
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Key is present in cache
        if key in self.cache:
            # Update the existing key's value
            self.cache[key] = value
            self.cache.move_to_end(key)
        # Key is not present in cache
        else:
            # Pop last item to make space
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            # Update cache
            self.cache[key] = value

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)