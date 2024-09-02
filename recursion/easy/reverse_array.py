class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr):
        # pass
        copy = arr
        
        def reverse(i, j):
            # our base case would be ->
            # if the pointers cross each other:
            if i > j:
                return
            # if not, swap:
            copy[i], copy[j] = copy[j], copy[i]
            # call reverse by incrementing the left
            # pointer and decrementing the right pointer:
            reverse(i + 1, j - 1)
        
        reverse(0, len(copy) - 1)
        
        return copy
    
    def solver2(self, arr):
        copy = arr
        n = len(copy)
        
        def reverse(i):
            # base case:
            if i >= n // 2:
                return
            # processing:
            copy[i], copy[n - i - 1] = copy[n - i - 1], copy[i]
            # our recursive call:    
            reverse(i + 1)
        
        reverse(0)
        
        return copy
            
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([1, 2, 3, 4, 2]))
    print(solver.solver([2, 3, 4, 1, 2, 1]))
    print(solver.solver2([1, 2, 3, 4, 2]))
    print(solver.solver2([2, 3, 4, 1, 2, 1]))

if __name__ == "__main__":
    main()