import random

class RandomizedSet:
    def __init__(self):
        self.randomSet = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.randomSet.append(val)
            self.indices[val] = len(self.randomSet) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index_to_remove = self.indices[val]
            last_element = self.randomSet[-1]
            self.randomSet[index_to_remove] = last_element
            self.indices[last_element] = index_to_remove
            self.randomSet.pop()
            del self.indices[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.randomSet)