class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    # list stuff
    def createFromArr(arr):
        current = Node(arr[0])
        head = current
        
        for i in range(1, len(arr)):
            current.next = Node(arr[i])
            current = current.next
        
        return head

    def printList(head):
        current = head
        print("[", end = "")
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None ]")
        
    def append(listHead, data):
        if not listHead:
            return Node(data)
        
        current = listHead
        
        while current.next != None:
            current = current.next
        
        current.next = Node(data)
        
        return listHead
    
    arr = [1, 2, 3, 4, 5]
    h1 = createFromArr(arr)
    printList(h1)
    
    h1 = append(h1, 10)
    printList(h1)
    
    h2 = createFromArr([340])
    printList(h2)
    
    printList(append(h2, 1))
    
    
if __name__ == "__main__":
    main()