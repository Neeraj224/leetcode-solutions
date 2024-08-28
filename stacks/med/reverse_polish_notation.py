import math
class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, tokens):
        # pass
        stack = []
        operations = "+-/*"
        
        for token in tokens:
            if token in operations:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                result = 0
                
                if token == "+":
                    result = num1 + num2
                if token == "-":
                    result = num1 - num2
                if token == "*":
                    result = num1 * num2
                if token == "/":
                    result = math.trunc(num1 / num2)
                
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack[0])
                    

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(tokens = ["2","1","+","3","*"]))
    print(solver.solver(tokens = ["4","13","5","/","+"]))
    print(solver.solver(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(solver.solver(tokens = ["4","-2","/","2","-3","-","-"]))
    

if __name__ == "__main__":
    main()