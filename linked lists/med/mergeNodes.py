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
    
def mergeNodes(head):
    free = head.next
    currsum = 0
    newHead = Node(9999)
    newCurrent = newHead
    
    while free:
        if free.data == 0:
            newCurrent.next = Node(currsum)
            newCurrent = newCurrent.next
            currsum = 0
            free = free.next
        else:
            currsum += free.data
            free = free.next
    
    newHead = newHead.next
    
    return newHead
            
 
def main():
    # driver code
    list1 = constructFromArray(arr = [0,3,1,0,4,5,2,0])
    # list2 = constructFromArray(arr = [0,1,0,3,0,2,2,0])
    list2 = constructFromArray(arr = [0,1,0])
    
    printList(list1)
    # printList(list2)
    
    printList(mergeNodes(list1))
    printList(mergeNodes(list2))
    
if __name__ == "__main__":
    main()