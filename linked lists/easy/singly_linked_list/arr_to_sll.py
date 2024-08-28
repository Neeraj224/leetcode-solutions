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
    
def main():
    # driver code
    list1 = constructFromArray(arr = [1, 2, 3, 4, 5])
    list2 = constructFromArray(arr = [2, 4, 6, 7, 5, 1, 0])
    
    printList(list1)
    printList(list2)
    
if __name__ == "__main__":
    main()