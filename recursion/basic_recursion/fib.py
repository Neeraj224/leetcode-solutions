class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        elif n > 1:
            return self.solver(n - 1) + self.solver(n - 2)  

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(2))
    print(solver.solver(3))
    print(solver.solver(7))

if __name__ == "__main__":
    main()