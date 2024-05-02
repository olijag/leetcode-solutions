# https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.deque = []
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map.keys:
            return -1
        
        return self.deque[self.map[key]]

    def put(self, key: int, value: int) -> None:
        # If key is not present in the cache
        if key not in self.map.keys():
            # Cache is full
            if len(self.deque) == self.capacity:
                # Delete least recently used 
                last_element = self.deque[-1]
                pop_last_element = self.deque.pop()
                del self.map[last_element]
        
        # else present in the cache
        else: 
            del self.deque[self.map[key]]
        
        # Update cache
        self.deque.insert(0, value)
        self.map[key] = 0

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)