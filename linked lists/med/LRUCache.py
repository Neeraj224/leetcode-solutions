class ListNode:
    def __init__(self, key = -1, val = -1, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.LRUPointer = self.head

    def insertNode(self, node):
        

    # def showLRUCacheContents(self):
        current = self.head
        
        print("[None] <=> ", end = "")
        while current:
            print("[" + str(current.key) + ", " + str(current.val) + "]", end = "<=>")
            current = current.next
        print(" [None]")        
        
    def get(self, key: int) -> int:
        # def linear_scan(key):
        #     return key
        # return linear_scan(key)
        self.showLRUCacheContents()

    def put(self, key: int, value: int) -> None:
        self.showLRUCacheContents()

def main():
    """
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    """
    lrucache1 = LRUCache(2)
    
    lrucache1.put(1, 1)
    print(lrucache1.capacity)
    
    lrucache1.put(2, 2)
    print(lrucache1.capacity)
    
    lrucache1.put(3, 3)
    print(lrucache1.capacity)
    
    lrucache1.put(4, 4)
    print(lrucache1.capacity)
    
    lrucache1.showLRUCacheContents()
    

if __name__ == "__main__":
    main()