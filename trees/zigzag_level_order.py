class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def createTree(arr, i, n):
    root = None
    
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = createTree(arr, 2 * i + 1, n)
        root.right = createTree(arr, 2 * i + 2, n)
    
    return root

def traverse(root):
    traversal = []
    
    def inorder(root):
        if root is None:
            return
        
        inorder(root.left)
        traversal.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return traversal

def levelOrder(root):
    traversal = []
    
    if root is None:
        return traversal
    
    queue = []
    # push the root first
    queue.append(root)
    
    while len(queue) > 0:
        current = queue[0]
        # if theres a left child:
        if current.left:
            # append it to the queue
            queue.append(current.left)
        # if there is a right child:
        if current.right:
            # append it to the queue:
            queue.append(current.right)
        
        traversal.append(queue.pop(0).val)
        
    return traversal

def levelOrderLeet(root):
    traversal = []
    
    if root is None:
        return traversal
    
    queue = []
    # push the root first
    queue.append(root)
    
    while len(queue) > 0:
        level = []
        
        for _ in range(len(queue)):
            current = queue[0]
            # if theres a left child:
            if current.left:
                # append it to the queue
                queue.append(current.left)
            # if there is a right child:
            if current.right:
                # append it to the queue:
                queue.append(current.right)
            
            level.append(queue.pop(0).val)
        
        traversal.append(level)
        
    return traversal

def zigzagLevelOrder(root):
    zigzaglevels = levelOrderLeet(root)
    
    for i in range(len(zigzaglevels)):
        if i % 2 == 1:
            zigzaglevels[i] = list(reversed(zigzaglevels[i]))
    
    return zigzaglevels

def main():
    arr1 = [3,9,20,None,None,15,7]
    tree1 = createTree(arr1, 0, len(arr1))
    print(traverse(tree1))
    print(levelOrderLeet(tree1))
        
    arr2 = [1]
    tree2 = createTree(arr2, 0, len(arr2))
    print(traverse(tree2))
    print(levelOrderLeet(tree2))
    
    arr3 = []
    tree3 = createTree(arr3, 0, len(arr3))
    print(traverse(tree3))
    print(levelOrderLeet(tree3))
    
    print(zigzagLevelOrder(tree1))
    print(zigzagLevelOrder(tree2))
    print(zigzagLevelOrder(tree3))

if __name__ == "__main__":
    main()