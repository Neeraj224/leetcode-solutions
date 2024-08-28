class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = None

def buildTreeRecursive(arr, i, n):
    """
        # arr is the list we will build with; i is the current
        # index we're at in the array.
        # n is the total length of the array
    """
    root = None
    
    if i < n and arr[i] is not None:
        # for the ith position in the array
        root = TreeNode(arr[i])
        # its left child will be at the (2*i + 1) position
        root.left = buildTreeRecursive(arr, (2 * i) + 1, n)
        # and its right child will be at the (2*i + 2) position
        root.right = buildTreeRecursive(arr, (2 * i) + 2, n)
    
    return root

def buildTreeIterative(arr):
    # obviously if the array is empty:
    if len(arr) == 0:
        # return Nothing
        return None
    
    # this is the queue that will store the nodes temporarily
    nodes = []
    # we take the first element of the array
    val = arr.pop(0)
    # and make it the root node
    root = TreeNode(val)
    nodes.append(root)
    
    # while there are elements in the array:
    while len(arr) > 0:
        curr = nodes.pop(0)
        
        left_val = arr.pop(0)
        
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)
            
        if len(arr) > 0:
            right_val = arr.pop(0)
            
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)
    
    return root

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def preorder(root):
    if not root:
        return
    
    print(root.val, end = " ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val, end = " ")

def main():
    arr1 = [i for i in range(10)]
    arr2 = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]
    
    tree1 = buildTreeRecursive(arr1, 0, len(arr1))
    tree2 = buildTreeRecursive(arr2, 0, len(arr2))
    
    print("inorder traversal: ", end = "")    
    inorder(tree1)
    print("")
    
    print("preorder traversal: ", end = "")    
    preorder(tree1)
    print("")
    
    print("postorder traversal: ", end = "")    
    postorder(tree1)
    print("")
    
    tree1 = buildTreeIterative(arr1)
    print("inorder traversal: ", end = "")    
    inorder(tree1)
    print("")
    
    print("preorder traversal: ", end = "")    
    preorder(tree1)
    print("")
    
    print("postorder traversal: ", end = "")    
    postorder(tree1)
    print("")
    
    
if __name__ == "__main__":
    main()