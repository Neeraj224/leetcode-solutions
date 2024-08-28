class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n, rsum):
        if n > 0:
            rsum += n * n * n
            return self.solver(n - 1, rsum)
        
        return rsum
    
    def solver_one_param(self, n):
        if n == 0:
            return 0
        
        return (n * n * n) + self.solver_one_param(n - 1)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5, 0))
    print(solver.solver(7, 0))
    print(solver.solver_one_param(5))
    print(solver.solver_one_param(7))

if __name__ == "__main__":
    main()