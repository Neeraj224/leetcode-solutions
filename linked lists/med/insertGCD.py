import math

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
    
def insertGreatestCommonDivisors(head):
    if head.next == None:
        return head
    
    one = head
    two = one.next
    
    while two:
        newNode = Node(math.gcd(one.data, two.data))
        newNode.next = one.next
        one.next = newNode
        one = one.next.next
        two = two.next
    
    return head

def main():
    # driver code
    list1 = constructFromArray(arr = [18,6,10,3])
    list2 = constructFromArray(arr = [7])
    
    printList(list1)
    printList(list2)
    
    printList(insertGreatestCommonDivisors(list1))
    printList(insertGreatestCommonDivisors(list2))
    
    
if __name__ == "__main__":
    main()