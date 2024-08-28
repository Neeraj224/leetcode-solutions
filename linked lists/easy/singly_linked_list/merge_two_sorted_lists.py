class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
        
def createListFromArray(arr):
    if len(arr) == 0:
        return arr
    
    head = ListNode(arr[0])
    
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head
    
def printList(head):
    if not head:
        return None
    
    current = head
    print("[ ", end = "")
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print(" None ]")

# def reverseList(head):
#     prev = None
#     current = head
    
#     while current:
#         temp = current.next
#         current.next = prev
#         prev = current
#         current = temp
    
#     return prev

def mergeTwoLists(list1, list2):
    newHead = current = ListNode()
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    newHead = newHead.next
    return newHead
    

def main():
    arr11 = [1,2,4]
    arr12 = [1,3,4]
    list1 = createListFromArray(arr11)
    list2 = createListFromArray(arr12)
    
    arr21 = []
    arr22 = []
    list3 = createListFromArray(arr21)
    list4 = createListFromArray(arr22)
    
    arr31 = []
    arr32 = [0]
    list5 = createListFromArray(arr31)
    list6 = createListFromArray(arr32)
    
    printList(mergeTwoLists(list1, list2))
    # printList(mergeTwoLists(list3, list4))
    printList(mergeTwoLists(list5, list6))
    
    # printList(reverseList(list1))
    # printList(reverseList(list2))
    # printList(reverseList(list3))
    
if __name__ == "__main__":
    main()
        