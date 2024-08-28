import math

class Node:
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = None
        self.random = None

def createList(arr) -> Node:
    if len(arr) == 0:
        return None
    
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return head


def printList(head):
    if head is None:
        return None
    
    current = head
    print("[ ", end = "")
    
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print(" None ]")

def createCopyOfList(head):
    copy = Node()
    currentCopy = copy
    
    if not head:
        copy = head
        return copy
    
    current = head
    
    while current:
        currentCopy.next = Node(current.val)
        current = current.next
        currentCopy = currentCopy.next
    
    copyHead = copy.next
    copy.next = None
    
    return copyHead

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [1, 2, 3, 4, 5]
    
    list1 = createList(arr1)
    list2 = createList(arr2)
    
    printList(list1)
    printList(list2)
    
    printList(createCopyOfList(list1))
    
    
if __name__ == "__main__":
    main()