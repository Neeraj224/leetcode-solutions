class Solution:
    def __init__(self) -> None:
        pass
    
    def problem(self, x: int):
        if x < 0:
            return False
        if x < 10:
            return True
        
        str_x = str(x)
        left = 0
        right = len(str_x) - 1
        
        palindrome_flag = False
        
        while left <= right:
            if str_x[left] != str_x[right]:
                palindrome_flag = False
                break
            else:
                palindrome_flag = True
                left += 1
                right -= 1
        
        return palindrome_flag

def main():
    solver = Solution()
    
    print(solver.problem(8))
    print(solver.problem(121))
    print(solver.problem(-121))
    print(solver.problem(10))

if __name__ == "__main__":
    main()