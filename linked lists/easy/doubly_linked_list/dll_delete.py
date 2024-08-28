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

def delete(head, pos):
    curr_pos = 1 
    current = head
    
    # case 1: if deleting at head
    if pos == 1:
        head = current.next
        head.prev.next = None
        head.prev = None
        return head
    
    # traverse the list to get to the position:
    while pos != curr_pos:
        current = current.next
        curr_pos += 1
    
    # case 2: if deleting at the tail:
    if current.next == None:
        current.prev.next = None
        current.prev = None
    # case 3: if deleting anywhere else:
    else:
        current.prev.next = current.next
        current.next.prev = current.prev
        current.next = None
        current.prev = None
    
    return head

def main():
    # driver
    dll1 = create([1, 2, 3, 4, 5])
    printList(dll1)
    reversePrint(dll1)
    
    dll1 = delete(dll1, 5)
    printList(dll1)
            

if __name__ == "__main__":
    main()