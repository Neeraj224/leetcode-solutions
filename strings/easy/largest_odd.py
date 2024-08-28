class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, num):
        odd = ""
        
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                odd = num[:i + 1]
                break
        
        return odd
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(num = "52"))
    print(solver.solver(num = "4206"))
    print(solver.solver(num = "35427"))

if __name__ == "__main__":
    main()