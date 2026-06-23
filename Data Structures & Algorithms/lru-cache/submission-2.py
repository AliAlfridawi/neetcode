class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                self.cache.append([key,value])
                return
        
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        self.cache.append([key,value])
        return
