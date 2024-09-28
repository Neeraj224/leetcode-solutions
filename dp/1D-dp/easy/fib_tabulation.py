class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        # pass
        dp = [0] * (n + 2)
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3, n + 2):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5))
    print(solver.solver(14))
    # print(solver.solver())

if __name__ == "__main__":
    main()