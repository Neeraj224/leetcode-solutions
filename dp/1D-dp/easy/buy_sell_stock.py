class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, prices):
        # pass
        n = len(prices)
        currentmax = float('-inf')
        def maximize(prices, n):
            nonlocal currentmax
            if n == 0:
                return currentmax

            for i in range(n - 1, -1, -1):
                currentmax = max(prices[n - 1] - prices[i], currentmax)
                
            maximize(prices, n - 1)
            
            return currentmax

        return maximize(prices, n)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(prices = [7,1,5,3,6,4]))
    print(solver.solver(prices = [7,6,4,3,1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()