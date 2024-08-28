class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

def create(arr):
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current.next.prev = current
        current = current.next
    
    return head

def printList(head):
    current = head
    
    print("[ ", end = "")
    while current:
        print(current.data, end = " <=> ")
        current = current.next
    print(" None ]")

def reversePrint(head):
    current = head
    
    while current.next != None:
        current = current.next
    
    print("[ None", end = "")
    while current:
        print(" <=> ", end = "")
        print(current.data, end = "")
        current = current.prev
    print(" ]")

def reverseList(head):
    current = head
    left = current
    right = current
    length = 1
    
    while right.next != None:
        right = right.next
        length += 1
    
    print(right.data)
    
    if length % 2 == 1:
        middle = length // 2 + 1
    else:
        middle = length // 2
    
    i = 0
    
    while i < middle:
        left.data, right.data = right.data, left.data
        
        left = left.next
        right = right.prev
        
        i += 1
    
    return head
    
def main():
    # driver
    dll1 = create([1, 2, 3, 4, 5])
    printList(dll1)
    reversePrint(dll1)
    
    reverseList(dll1)
    printList(dll1)
            

if __name__ == "__main__":
    main()