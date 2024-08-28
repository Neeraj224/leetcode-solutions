class Solution:
    def __init__(self) -> None:
        pass
    
    def armstrong(self, n):
        str_n = str(n)
        power = len(str_n)
        armstrongness = 0
        
        for i in range(len(str_n)):
            armstrongness += int(str_n[i]) ** power
        
        return armstrongness == n

def main():
    solver = Solution()
    
    print(solver.armstrong(153))
    print(solver.armstrong(123))

if __name__ == "__main__":
    main()