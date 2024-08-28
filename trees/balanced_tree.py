class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
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
    inorder_res = []
    
    def inorder(root):
        if root is None:
            return
        
        inorder(root.left)
        inorder_res.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return inorder_res

def isBalanced(root):
    def dfs(root, depth):
        if not root:
            return depth
        
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    
    return dfs(root, 0)
    

def main():
    arr1 = [3,9,20,None,None,15,7]
    arr2 = [1,2,2,3,3,None,None,4,4]
    arr3 = []
    
    tree1 = createTree(arr1, 0, len(arr1))
    tree2 = createTree(arr2, 0, len(arr2))
    tree3 = createTree(arr3, 0, len(arr3))
    
    print(traverse(tree1))
    print(traverse(tree2))
    print(traverse(tree3))
    
    print(isBalanced(tree1))
    print(isBalanced(tree2))
    print(isBalanced(tree3))

if __name__ == "__main__":
    main()