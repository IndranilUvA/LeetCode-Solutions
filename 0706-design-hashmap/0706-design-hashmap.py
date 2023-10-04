class MyHashMap:

    def __init__(self):
        self.giant_list = [None for _ in range(1000001)]

    def put(self, key, value):
        self.giant_list[key] = value
      
    def get(self, key):
        return self.giant_list[key] if self.giant_list[key]!= None else -1

    def remove(self, key):
        if self.giant_list[key]:
            self.giant_list[key] = None 
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)