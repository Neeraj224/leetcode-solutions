class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s: str):
        res = ""
        balance = 0
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(":
                if balance > 0:
                    res += s[i]
                    balance += 1
                else:
                    stack.append(s[i])
                    balance += 1
            
            if s[i] == ")":
                if balance > 1:
                    res += s[i]
                    balance -= 1
                else:
                    stack.append(s[i])
                    balance -= 1
        
        print(stack)
        return res
                
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "(()())(())"))
    print(solver.solver(s = "(()())(())(()(()))"))
    print(solver.solver(s = "()()"))

if __name__ == "__main__":
    main()