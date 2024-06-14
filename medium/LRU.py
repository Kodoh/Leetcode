import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash=collections.OrderedDict()
    def get(self, key: int) -> int:
        if key in self.hash:
            self.hash.move_to_end(key)
            return self.hash[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key]=value
            self.hash.move_to_end(key)
        elif len(self.hash)==self.capacity:
            self.hash.popitem(last=False)
            self.hash[key]=value
        else:
            self.hash[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)