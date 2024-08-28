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

def getDecimalValue(head: ListNode):
    decimal = ""
    
    current  = head
    
    while current:
        decimal += str(current.val)
        current = current.next
    
    return int(decimal, 2)

def main():
    # driver code
    list1 = constructFromArray([1,0,1])
    list2 = constructFromArray([0])
    
    print(getDecimalValue(list1))
    print(getDecimalValue(list2))
    
    
    
    
if __name__ == "__main__":
    main()