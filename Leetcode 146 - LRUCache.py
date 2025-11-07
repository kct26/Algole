class Node: 
    def __init__ (self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        self.remove(self.mapping[key])
        self.insert(self.mapping[key])
        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            self.mapping[key].val = value
        else:
            if len(self.mapping) == self.capacity:
                del self.mapping[self.left.next.key]
                self.remove(self.left.next)
            temp = Node(key, value)
            self.mapping[key] = temp
            self.insert(temp)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
