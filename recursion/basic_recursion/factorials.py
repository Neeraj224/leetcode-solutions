class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        def fact(n):
            if n == 0:
                return 0
            return n + fact(n - 1)

        facts = []
        
        for i in range(1, n):
            if fact(i) <= n:
                facts.append(i)
        
        return facts
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(3))
    print(solver.solver(6))

if __name__ == "__main__":
    main()