class MinStack:
    def __init__(self):
        self.minstack = []
        self.stack = []
        # self.top = None
    
    def push(self, val) -> None:
        self.stack.append(val)

        if len(self.minstack) == 0:
            self.minstack.append(val)
        elif val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
    
# def main():
    
    
    
# if __name__ == "__main__":
#     main()