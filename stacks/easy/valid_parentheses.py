class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        if len(s) == 1:
            return False
        
        stack = []
        # lets get the first character on to the stack:
        stack.append(s[0])
        
        for i in range(1, len(s)):
            if s[i] == ")" and len(stack) != 0:
                if stack[-1] == "(":
                    stack.pop()
                    continue
            if s[i] == "]" and len(stack) != 0:
                if stack[-1] == "[":
                    stack.pop()
                    continue
            if s[i] == "}" and len(stack) != 0:
                if stack[-1] == "{":
                    stack.pop()
                    continue
            
            stack.append(s[i])
        
        return len(stack) == 0
        
                                  
def main():
    solver = Solution()
    
    # solver.solver()
    print(solver.solver(s = "()"))
    print(solver.solver(s = "()[]{}"))
    print(solver.solver(s = "(]"))

if __name__ == "__main__":
    main()