class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s1, s2):
        # pass
        windowsize = len(s1)
        s1sorted = sorted(s1)
        # tempmap = {}
        
        for i in range(0, len(s2) - windowsize + 1):
            temp = s2[i : i + windowsize]
            if s1sorted == sorted(temp):
                return True
            
        return False
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s1 = "ab", s2 = "eidbaooo"))
    print(solver.solver(s1 = "ab", s2 = "eidboaoo"))
    print(solver.solver(s1 = "adc", s2 = "dcda"))

if __name__ == "__main__":
    main()