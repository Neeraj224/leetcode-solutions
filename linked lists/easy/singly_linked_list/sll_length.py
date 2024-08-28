class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
def main():
    # driver
    def create(arr):
        head = Node(arr[0])
        curr = head
        
        for i in range(1, len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        
        return head

    def printList(head):
        curr = head
        
        print("[ ", end = "")
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None ]")
    
    def delete(head, target):
        curr = head
        
        while curr.next.data != target:
            curr = curr.next
        
        # get the one to be deleted in a temp variable
        deleted = curr.next
        # update pointer of the previous node to the next to the one being deleted:
        curr.next = curr.next.next
        # update pointer of the one to be deleted to None
        deleted.next = None
        
        return head
    
    def getLength(head):
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next
        
        return length
        
    h1 = create([1, 2, 3, 4, 5])
    printList(h1)
    print(getLength(h1))
    
    h1 = delete(h1, 3)
    printList(h1)
    
    print(getLength(h1))
    
if __name__ == "__main__":
    main()