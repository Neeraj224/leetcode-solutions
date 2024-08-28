class Solution:
    def __init__(self) -> None:
        pass
    
    def getNumber(self, n):
        numbers = []
        
        def generate(idx, n, current):
            if len(current) == n:
                numbers.append(current)
                return
            if idx == n + 1 and len(numbers) == n:
                return
            else:
                current += str(idx)
                generate(idx + 1, n, current)
            
        generate(1, n, "")
        return numbers
    
    def solver(self, n):
        return self.getNumber(n)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5))
    print(solver.solver(4))
    print(solver.solver(2))

if __name__ == "__main__":
    main()