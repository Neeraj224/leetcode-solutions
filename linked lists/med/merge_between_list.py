class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

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

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode):
    first = list1
    second = list1
    toDel = list1
    firstpos = 0
    secondpos = 0
    
    while firstpos != a - 1:
        first = first.next
        firstpos += 1
    
    while secondpos != b + 1:
        second = second.next
        secondpos += 1
    
    secondpos = 0
    while secondpos != b:
        toDel = toDel.next
        secondpos += 1
    
    toDel.next = None
    
    first.next = list2
    current = list2
    
    while current.next != None:
        current = current.next
    
    current.next = second

    return list1

def main():
    # driver code
    list1 = constructFromArray(arr = [10,1,13,6,9,5])
    list2 = constructFromArray(arr = [1000000,1000001,1000002])
    
    list3 = constructFromArray(arr = [0,1,2,3,4,5,6])
    list4 = constructFromArray(arr = [1000000,1000001,1000002,1000003,1000004])
    
    printList(mergeInBetween(list1, 3, 4, list2))
    printList(mergeInBetween(list3, 2, 5, list4))
    # mergeInBetween(list1, 3, 4, list2)
    
if __name__ == "__main__":
    main()