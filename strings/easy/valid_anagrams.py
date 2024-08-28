class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s, t):
        if len(s) != len(t):
            return False
        
        ns = ''.join(sorted(s))
        nt = ''.join(sorted(t))
        i = 0
        
        while i < len(ns):
            if ns[i] != nt[i]:
                return False
            i += 1
        
        return True
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "anagram", t = "nagaram"))
    print(solver.solver(s = "rat", t = "car"))
    # print(solver.solver())

if __name__ == "__main__":
    main()