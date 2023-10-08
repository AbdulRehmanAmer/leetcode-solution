
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.val = list()
        self.key = list()
        self.indices = dict()
        self.start = 0

    def get(self, key: int) -> int:
        if key not in self.indices: return -1
        

        i = self.indices[key]
        if self.val[i] == None: return -1
        get_value = self.val[i]


        self.indices[key] = len(self.val)
        self.val.append(self.val[i])
        self.key.append(key)

        self.start += 1

        return get_value


        

    def put(self, key: int, value: int) -> None:
        if key in self.indices:
            if self.indices[key] == 0:
                self.start += 1
            self.indices[key] = len(self.val)
            self.val.append(value)
            self.key.append(key)

            return None

       

        if not self.capacity:
            
            del self.indices[self.key[self.start]]
            self.start += 1
            self.indices[key] = len(self.val)

            self.val.append(value)
            self.key.append(key)

            return None
        
        self.indices[key] = len(self.val)

        self.val.append(value)
        self.key.append(key)
        self.capacity -= 1
        
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print (obj.get(1))
# obj.put(3, 3)
# print (obj.get(2))
# obj.put(4, 4)
# print (obj.get(1))
# print (obj.get(3))
# print (obj.get(4))


# obj = LRUCache(1)
# obj.put(2, 1)
# print (obj.get(2))
# obj.put(3, 2)
# print (obj.get(2))
# print (obj.get(3))

obj = LRUCache(2)
obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
print (obj.get(1))
print (obj.get(2))