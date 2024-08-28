class Solution:
    def __init__(self) -> None:
        pass
    
    def recPrint(self, n):
        if n > 0:
            self.recPrint(n - 1)
            print(n, end = " ")

def main():
    solver = Solution()
    
    print(solver.recPrint(10))
    print(solver.recPrint(20))

if __name__ == "__main__":
    main()