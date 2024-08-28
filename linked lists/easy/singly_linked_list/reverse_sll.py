class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def constructFromArray(arr):
    current = Node(arr[0])
    head = current
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return head

def printList(head):
    current = head
    print("[", end = " ")
    while current:
        print(current.data, end = " -> ")
        current = current.next
    
    print(None, end = " ]")
    print("")

def reverseList(head):
    if head is None or head == None:
        return head

    arr = []
    current = head
    
    while current:
        arr.append(current.val)
        current = current.next
    
    arr = list(reversed(arr))
    
    new_head = Node(arr[0])
    current = new_head

    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return new_head

def main():
    # driver code
    list1 = constructFromArray(arr = [1, 2, 3, 4, 5])
    list2 = constructFromArray(arr = [2, 4, 6, 7, 5, 6])
    
    printList(list1)
    printList(list2)
    
if __name__ == "__main__":
    main()