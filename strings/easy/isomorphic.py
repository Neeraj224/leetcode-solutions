class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s, t):
        strmp1 = []
        strmp2 = []
        
        for c in s:
            strmp1.append(s.index(c))
        
        for c in t:
            strmp2.append(t.index(c))
        
        if strmp1 == strmp2:
            return True

        return False
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "egg", t = "add"))
    print(solver.solver(s = "foo", t = "bar"))
    print(solver.solver(s = "paper", t = "title"))

if __name__ == "__main__":
    main()