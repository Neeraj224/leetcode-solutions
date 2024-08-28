class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
def buildTree(arr, i, n):
    root = None
    
    if i < n and (arr[i] != -1 and arr[i] is not None):
        root = TreeNode(arr[i])
        root.left = buildTree(arr, 2 * i + 1, n)
        root.right = buildTree(arr, 2 * i + 2, n)
    
    return root

def traversals(root):
    inorder_result = []
    preorder_result = []
    postorder_result = []
    
    def inorder(root, inorder_result):
        if not root:
            return
        
        inorder(root.left, inorder_result)
        inorder_result.append(root.val)
        inorder(root.right, inorder_result)
    
    def preorder(root, preorder_result):
        if not root:
            return
        
        preorder_result.append(root.val)
        preorder(root.left, preorder_result)
        preorder(root.right, preorder_result)
    
    def postorder(root, postorder_result):
        if not root:
            return
        
        postorder(root.left, postorder_result)
        postorder(root.right, postorder_result)
        postorder_result.append(root.val)

    inorder(root, inorder_result)
    preorder(root, preorder_result)
    postorder(root, postorder_result)
    
    return inorder_result, preorder_result, postorder_result

def main():
    arr = [1, 2, 3, -1, -1, -1, 6, -1, -1]
    tree1 = buildTree(arr, 0, len(arr))
    print(traversals(tree1))
    
if __name__ == "__main__":
    main()