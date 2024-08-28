class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createTree(arr, i, n):
    root = None
    
    if i < n  and arr[i] is not None:
        root = TreeNode(arr[i])
        
        root.left = createTree(arr, 2 * i + 1, n)
        root.right = createTree(arr, 2 * i + 2, n)
    
    return root

def traverse(root):
    result = []
    
    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    return result

def isSameTree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
def main():
    p1 = [1,2,3] 
    q1 = [1,2,3]
    
    p2 = [1,2]
    q2 = [1,None,2]
    
    p3 = [1,2,1]
    q3 = [1,1,2]
    
    p1tree = createTree(p1, 0, len(p1))
    q1tree = createTree(q1, 0, len(q1))
    
    p2tree = createTree(p2, 0, len(p2))
    q2tree = createTree(q2, 0, len(q2))
    
    p3tree = createTree(p3, 0, len(p3))
    q3tree = createTree(q3, 0, len(q3))
    
    print(isSameTree(p1tree, q1tree))
    print(isSameTree(p2tree, q2tree))
    print(isSameTree(p3tree, q3tree))
    
    p = [1, 1]
    q = [1, None, 1]

    ptree = createTree(p, 0, len(p))
    qtree = createTree(q, 0, len(q))
    
    print(isSameTree(ptree, qtree))
    
    
    
if __name__ == "__main__":
    main()