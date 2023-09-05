class RandomizedSet:

    def __init__(self):
        self.hash_table = dict()
        self.idx = list()
        
    def insert(self, val: int) -> bool:
        if val in self.hash_table:
            return False
        self.hash_table[val] = len(self.hash_table)
        self.idx += [val]
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            index = self.hash_table[val]
            self.idx[index] = self.idx[-1]
            self.hash_table[self.idx[index]] = index
            self.idx.pop()
            del self.hash_table[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.idx)
    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()