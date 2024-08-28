class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        def countNodesAtHeightN(n):
            # for a binary tree, the number of nodes at height n
            # is 2^(n - 1)
            return 2 ** (n - 1)
        
        return countNodesAtHeightN(n)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5))
    print(solver.solver(1))
    print(solver.solver(8))

if __name__ == "__main__":
    main()