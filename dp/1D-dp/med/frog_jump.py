class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, energy):
        n = len(energy)
        # pass
        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            first_step = dp[i - 1] + abs(energy[i] - energy[i - 1])
            
            second_step = float('inf')
            
            if i > 1:
                second_step = dp[i - 2] + abs(energy[i] - energy[i - 2])
            
            dp[i] = min(first_step, second_step)
        
        return dp[-1]
            
def main():
    solver = Solution()
    
    print(solver.solver([10, 20, 30, 10]))
    print(solver.solver([30, 10, 60, 10, 60, 50]))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()