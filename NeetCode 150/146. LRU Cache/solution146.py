# https://leetcode.com/problems/lru-cache/description/

class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 1: 
            print("Error: Cache size must be bigger or equal 1")
            return None

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass