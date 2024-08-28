class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, accounts):
        # pass
        maxWealth = float('-inf')

        for i in range(len(accounts)):
            currentCustomerWealth = 0
            for j in range(len(accounts[i])):
                currentCustomerWealth += accounts[i][j]
            
            if currentCustomerWealth > maxWealth:
                maxWealth = max(maxWealth, currentCustomerWealth)
        
        return maxWealth

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(accounts = [[1,2,3],[3,2,1]]))
    print(solver.solver(accounts = [[1,5],[7,3],[3,5]]))
    print(solver.solver([[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == "__main__":
    main()
