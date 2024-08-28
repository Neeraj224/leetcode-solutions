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

def reverseList(head):
    prev = None
    current = head
    
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev

def main():
    arr1 = [1,2,3,4,5]
    arr2 = [1,2]
    arr3 = []
    
    list1 = createListFromArray(arr1)
    list2 = createListFromArray(arr2)
    list3 = createListFromArray(arr3)
    
    printList(list1)
    printList(list2)
    printList(list3)
    
    printList(reverseList(list1))
    printList(reverseList(list2))
    printList(reverseList(list3))
    
if __name__ == "__main__":
    main()
        