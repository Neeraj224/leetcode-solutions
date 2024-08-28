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
     
def reorderArray(arr) -> list:
    reorderedArray = []
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if left == right:
            reorderedArray.append(arr[left])
            break
        
        reorderedArray.append(arr[left])
        reorderedArray.append(arr[right])
        left += 1
        right -= 1
        
    return reorderedArray

def printList(head):
    if head is None:
        return None
    
    current = head
    print("[ ", end = "")
    
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print(" None ]")

def reOrderList(head):
    # head = self.createList(self.reorderArray(self.getArray(head)))
    # get the middle of the list:
    if not head:
        return None

    slow = head
    fast = slow.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # middle will be the slow.next
    middle = slow.next
    # we need to make the middle one point to None:
    slow.next = None

    # now we reverse the right half of the list:
    prev = None
    current = middle

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    middle = prev
    
    rightHead = prev
    leftHead = head

    while rightHead:
        leftTemp = leftHead.next
        rightTemp = rightHead.next
        leftHead.next = rightHead
        rightHead.next = leftTemp
        leftHead = leftTemp
        rightHead = rightTemp
    
    return head

def main():
    arr1 = [1,2,3,4]
    arr2 = [1,2,3,4,5]
    
    list1 = createList(arr1)
    list2 = createList(arr2)
    
    printList(list1)
    printList(list2)
    
    printList(createList(reorderArray(getArray(list1))))
    printList(createList(reorderArray(getArray(list2))))
    
    printList(reOrderList(list2))    
    
    
if __name__ == "__main__":
    main()