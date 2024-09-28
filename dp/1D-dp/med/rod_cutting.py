class Solution:
    def __init__(self) -> None:
        pass
    
    # Recursive approach (brute force)
    def rodCuttingRecursive(self, price, n):
        if n == 0:
            return 0
        max_value = float('-inf')
        for i in range(1, n + 1):
            max_value = max(max_value, price[i - 1] + self.rodCuttingRecursive(price, n - i))
        return max_value

    # Memoization (top-down DP)
    def rodCuttingMemo(self, price, n, memo):
        if n == 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        
        max_value = float('-inf')
        for i in range(1, n + 1):
            max_value = max(max_value, price[i - 1] + self.rodCuttingMemo(price, n - i, memo))
        
        memo[n] = max_value
        return max_value

    # Bottom-Up DP approach
    def rodCuttingBottomUp(self, price, n):
        dp = [0] * (n + 1)
        
        for length in range(1, n + 1):
            max_value = float('-inf')
            for cut in range(1, length + 1):
                max_value = max(max_value, price[cut - 1] + dp[length - cut])
            dp[length] = max_value
        
        return dp[n]

def main():
    solver = Solution()
    
    # Example 1:
    length1 = 8
    price1 = [1, 5, 8, 9, 10, 17, 17, 20]

    # Recursive approach
    print("Recursive Solution:", solver.rodCuttingRecursive(price1, length1))
    
    # Memoization approach
    memo1 = [-1] * (length1 + 1)
    print("Memoization Solution:", solver.rodCuttingMemo(price1, length1, memo1))
    
    # Bottom-Up DP approach
    print("Bottom-Up DP Solution:", solver.rodCuttingBottomUp(price1, length1))

if __name__ == "__main__":
    main()
