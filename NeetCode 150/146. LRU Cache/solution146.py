# https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 1: 
            print("Error: Cache size must be bigger or equal 1")
            return None
        
        self.capacity = capacity

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)