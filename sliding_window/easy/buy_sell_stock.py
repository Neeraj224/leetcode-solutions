class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, prices):
        # pass
        # maxProfit = 0
        # dp = []
        
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] < prices[j]:
        #             if (prices[j] - prices[i]) in dp:
        #                 continue
        #             # print(prices[j] - prices[i])
        #             dp.append(max(prices[j] - prices[i], maxProfit))
                    
        # if len(dp) == 0:
        #     return 0
        # return max(dp)
        profit = 0
        
        lowest = prices[0]
        
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        
        return profit
                

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(prices = [7,1,5,3,6,4]))
    print(solver.solver(prices = [7,6,4,3,1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()