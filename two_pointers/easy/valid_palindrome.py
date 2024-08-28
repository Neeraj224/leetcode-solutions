class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        condensed = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                condensed += c.lower()
        
        left = 0
        right = len(condensed) - 1
        
        while left <= right:
            if condensed[left] != condensed[right]:
                return False
            left += 1
            right -= 1
        
        return True
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "A man, a plan, a canal: Panama"))
    print(solver.solver(s = "race a car"))
    print(solver.solver(s = " "
))

if __name__ == "__main__":
    main()