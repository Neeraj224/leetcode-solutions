class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        # first we initalise our dp table with n + 1 len,
        # since we are gonna be summing the current cell with the
        # previous one
        dp_arr = [0] * (n + 1)
        
        # our recursive dp function:
        def dp(n):
            # base case:
            if n != 0:
                # until base case is reached, keep going
                dp(n - 1)
            
            # once the base case is reached, we will tabulate
            # the current sum at the nth position
            # by summing n and the previous number that is -> arr[n - 1]:
            dp_arr[n] = n + dp_arr[n - 1]
        
        # call dp on n:
        dp(n)
        
        # our final sum will be at the n - 1 index, so we return
        # the last index of the dp table:
        return dp_arr[-1]

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(10))
    print(solver.solver(100))
    print(solver.solver(5))

if __name__ == "__main__":
    main()