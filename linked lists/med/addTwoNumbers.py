class ListNode:
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = None
        self.random = None

def createList(arr) -> ListNode:
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

def printList(head):
    if head is None:
        return None
    
    current = head
    print("[ ", end = "")
    
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print(" None ]")

"""########################################################################"""
"""########################################################################"""

def addTwoNumbers(l1, l2):
    carryOver = 0
    
    cl1 = l1
    cl2 = l2
    
    resultList = ListNode(0, None)
    crl = resultList
    
    while cl1 and cl2:
        if carryOver == 0:
            rsum = cl1.val + cl2.val
        else:
            rsum = cl1.val + cl2.val + carryOver
            carryOver = 0
            
        if rsum >= 10:
            carryOver = int(str(rsum)[:1])
            toAdd = rsum % 10
        else:
            toAdd = rsum
            
        crl.next = ListNode(toAdd)
        crl = crl.next
        
        cl1 = cl1.next
        cl2 = cl2.next
    
    if carryOver and not cl1 and not cl2:
        crl.next = ListNode(carryOver)
        crl = crl.next
        carryOver = 0
    
    if cl1:
        while cl1:
            if carryOver == 0:
                crl.next = ListNode(cl1.val)
            else:
                rsum = cl1.val + carryOver
                carryOver = 0
                
                if rsum >= 10:
                    carryOver = int(str(rsum)[:1])
                    toAdd = rsum % 10
                else:
                    toAdd = rsum
                
                crl.next = ListNode(toAdd)
            
            cl1 = cl1.next
            crl = crl.next
    
    if cl2:
        while cl2:
            if carryOver == 0:
                crl.next = ListNode(cl2.val)
            else:
                rsum = cl2.val + carryOver
                carryOver = 0
                
                if rsum >= 10:
                    carryOver = int(str(rsum)[:1])
                    toAdd = rsum % 10
                else:
                    toAdd = rsum
                
                crl.next = ListNode(toAdd)
            
            cl2 = cl2.next
            crl = crl.next
    
    if carryOver and not cl1 and not cl2:
        crl.next = ListNode(carryOver)
        crl = crl.next
    
    resultList = resultList.next
      
    return resultList

def main():
    arr1 = [9,9,9,9,9,9,9]
    arr2 = [9,9,9,9]
    
    list1 = createList(arr1)
    list2 = createList(arr2)
    
    printList(list1)
    printList(list2)
    
    printList(addTwoNumbers(list1, list2))    
    
    
if __name__ == "__main__":
    main()