class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def constructFromArray(arr):
    current = ListNode(arr[0])
    head = current
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

def printList(head):
    current = head
    print("[", end = " ")
    while current:
        print(current.val, end = " -> ")
        current = current.next
    
    print(None, end = " ]")
    print("")

def removeNodes(head):
    current = head
    # head of the DLL:
    doubleHead = DoubleNode(current.val)
    # current pointer to build the DLL:
    currentDouble = doubleHead
    
    if current.next is None:
        return doubleHead
    else:
        current = current.next
    
    while current:
        newNode = DoubleNode(current.val)
        newNode.prev = currentDouble
        currentDouble.next = newNode
        # increment:
        currentDouble = currentDouble.next
        current = current.next
    
    current = doubleHead
    
    while current.next != None:
        current = current.next

    maximus = []
    currmax = current.val
    
    while current:
        if current.prev is None:
            if current.val > currmax:
                break
            elif current.val == currmax:
                maximus.append(current.val)
                break
        elif current.val > current.prev.val:
            maximus.append(current.val)
            currmax = max(current.val, currmax)
        elif current.val == current.prev.val:
            maximus.append(current.val)
        current = current.prev

    return constructFromArray(list(reversed(maximus)))
    
def main():
    # driver code
    list1 = constructFromArray([5,2,13,3,8])
    list2 = constructFromArray([1, 1, 1, 1])
    list3 = constructFromArray([1])

    printList(removeNodes(list1))
    printList(removeNodes(list2))
    printList(removeNodes(list3))
    
    
    

if __name__ == "__main__":
    main()