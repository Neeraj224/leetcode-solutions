class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        def palindrome_check(i, j):
            # our base case is if the pointers
            # have crossed:
            if i > j:
                # if they, that means we have reached the
                # end of the string and all was same,
                # so we can say that the string was a palindrome:
                return True
            
            # if we find any character that is not equal
            # to its symmetric index in the sequence, then the 
            # string is not a palindrome so lets return False
            # this is our processing step:
            if s[i] != s[j]:
                return False
            
            # now we do our recursive call:
            return palindrome_check(i + 1, j - 1)
        
        # call from the start and the end:
        return palindrome_check(0, len(s) - 1)
            
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver("sqssqs"))
    print(solver.solver("haha"))
    print(solver.solver("msm"))

if __name__ == "__main__":
    main()