import math

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

def createList(arr) -> ListNode:
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

def getArray(head) -> list:
    listElements = []
    
    if not head:
        return []
    
    current = head
    
    while current:
        listElements.append(current.val)
        current = current.next
    
    return listElements

def printList(head):
    if head is None:
        return None
    
    current = head
    print("[ ", end = "")
    
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print(" None ]")

def removeNthFromEnd(head, n):
    # first we check what happens if we start counting the slow and fast pointers
    # while finding the mid node of the list:

    slow = head
    fast = head.next
    slowCount = 0
    fastCount = 0
    
    while fast and fast.next:
        # print("slow is at: " + str(slow.val) + ", fast is at: " + str(fast.val))
        slowCount += 1
        fastCount += 2
        
        slow = slow.next
        fast = fast.next.next
    
    slowCount += 1
    
    totalNodes = 0
    if fast is not None:
        totalNodes = fastCount + 2
    else:
        totalNodes = fastCount + 1
    
    if n == totalNodes and n == 1:
        head = None
        return head
    
    if n < math.ceil(totalNodes / 2):
        nodeToRemove = (totalNodes - n) + 1  
        while slowCount != nodeToRemove and slow:
            slow = slow.next
            slowCount += 1
    else:
        slow = head
        slowCount = 1
        nodeToRemove = (totalNodes - n) + 1  
        while slowCount != nodeToRemove and slow:
            slow = slow.next
            slowCount += 1
    
    # print(slow.val)
    nthNode = slow
    
    temp = head
    if temp != nthNode:
        while temp.next != nthNode and temp and nthNode:
            temp = temp.next
    
        temp.next = nthNode.next
        nthNode.next = None
    else:
        head = temp.next
        temp.next = None
    
    return head

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [1, 2, 3, 4, 5]
    
    list1 = createList(arr1)
    list2 = createList(arr2)
    
    printList(list1)
    printList(list2)
    
    printList(removeNthFromEnd(list1, 6))
    printList(removeNthFromEnd(list1, 1))
    printList(removeNthFromEnd(list1, 2))
    
    
    
if __name__ == "__main__":
    main()