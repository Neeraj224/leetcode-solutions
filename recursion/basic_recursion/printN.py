class Solution:
    def __init__(self) -> None:
        pass
    
    def recPrint(self, n):
        if n == 0:
            return
        else:
            print(n, end = " ")
            self.recPrint(n - 1)

def main():
    solver = Solution()
    
    print(solver.recPrint(10))

if __name__ == "__main__":
    main()