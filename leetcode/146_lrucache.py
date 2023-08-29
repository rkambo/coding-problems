class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None
        
class LRUCache:
        
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        
        self.lru.nxt = self.mru
        self.mru.prev = self.lru

    def remove(self, node):
        prev,nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        
    def insert(self, node):
        prev, nxt = self.mru.prev,self.mru
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev,nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.lru.nxt
            self.remove(lru)
            del self.cache[lru.key]