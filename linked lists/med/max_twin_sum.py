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

def length(head):
    current = head
    length = 0
    
    while current:
        length += 1
        current = current.next
    
    return length

def reverseList(head):
    if head is None or head == None:
        return head

    arr = []
    current = head
    
    while current:
        arr.append(current.val)
        current = current.next
    
    arr = list(reversed(arr))
    
    new_head = ListNode(arr[0])
    current = new_head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return new_head

def pairSum(head):
    # step 1: we cut the linked list into two halves:
    current = head
    n = length(current)
    i = 0
    
    while i != (n // 2) - 1:
        current = current.next
        i += 1
    
    # our new list will be in head2
    head2 = current.next
    # make the current point to None, so that it is a list in itself:
    current.next = None
    
    # step 2: reverse the new (second) list:
    head2 = reverseList(head2)

    # step 3: get twin sums using two pointers:
    list1 = head
    list2 = head2
    currsum = -1
    
    while list1 and list2:
        twinsum = list1.val + list2.val
        currsum = max(twinsum, currsum)
        list1 = list1.next
        list2 = list2.next
    
    return currsum
    
def main():
    # driver code
    list1 = constructFromArray([5,4,2,1])
    list2 = constructFromArray([4,2,2,3])
    list3 = constructFromArray([1,100000])
    
    print(pairSum(list1))
    print(pairSum(list2))
    print(pairSum(list3))
    

if __name__ == "__main__":
    main()