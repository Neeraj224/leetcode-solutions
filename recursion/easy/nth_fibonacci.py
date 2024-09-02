class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        # pass
        def fibonacci(n):
            if n < 3:
                return 1
            
            return fibonacci(n - 1) + fibonacci(n - 2)
        
        return fibonacci(n)
    
    def solver2(self, n):
        dp = [0] * (n + 1)
        dp[-1] = 0
        dp[-2] = 1
        
        def fibonacci(n):
            if n <= 1:
                return n
            
            dp[n - 2] = dp[n - 1] + dp[n]
            
            return fibonacci(n - 1) + fibonacci(n - 2)
        
        result = fibonacci(n)
        print(dp)
        
        return result

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver2(4))
    print(solver.solver2(5))
    print(solver.solver2(8))

if __name__ == "__main__":
    main()