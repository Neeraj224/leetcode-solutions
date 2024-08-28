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
    
    print("None ]")
    
def printReverse(head):
    current = head
    
    while current.next != None:
        current = current.next
    
    print("[ None", end = "")
    while current:
        print(" <=> ", end = "")
        print(current.data, end = "")
        current = current.prev
    print(" ]")

def main():
    # driver code
    list1 = create([1, 2, 3, 4, 5])
    printList(list1)
    printReverse(list1)

    
if __name__ == "__main__":
    main()