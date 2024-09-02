class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        # pass
        # if its zero or one,
        # return those:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [-1] * (n + 1)

        def f(n):
            if n <= 1:
                return n
            # if it was already saved, get it:
            if dp[n] != -1:
                # and then just return that,
                # instead of going for further recursive calls
                return dp[n]
            # if its not present, then just save it, and then
            dp[n] = f(n - 1) + f(n - 2)
            # and return that:
            return dp[n]

        # call f() on n:
        f(n)
        # our result will be saved in the last index:
        return dp[-1]
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5))
    print(solver.solver(25))
    # print(solver.solver())

if __name__ == "__main__":
    main()