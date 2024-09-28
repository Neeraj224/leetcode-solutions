class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n):
        # pass
        ways = []
        
        def backtrack(n, current):
            # base cases
            # if it goes below 0, i.e. negative,
            # then just return
            if n < 0:
                return
            # if its zero, we found a valid path
            # so append it to our master ways
            if n == 0:
                if current not in ways:
                    ways.append(current[:])
                # and then return
                return

            # now first we append 1 to the path:
            # i.e., we take it:
            current.append(1)
            # deduct it from our n:
            n -= 1
            # and then recursively check this path:
            backtrack(n, current)
            # once it has been explored, then pop() it:
            current.pop()
            # and then add the 1 we deducted from n previously
            n += 1
            
            # now we explore the path if we take 2:
            current.append(2)
            # do all the same things we did with our first path:
            n -= 2
            backtrack(n, current)
            current.pop()
            n += 2
        
        backtrack(n, [])
        print(ways)
        return len(ways)
    
    def solver2(self, n):
        dp = [0] * (n + 1)
        
        def count(n):
            if n == 0:
                return 1
            if n == 1:
                return 0
            
            if dp[n] != 0:
                return dp[n]
            
            left = count(n - 1)
            right = count(n - 2)
            
            return left + right
            
            
        print(dp)
        return count(n)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver2(4))
    print(solver.solver2(3))
    print(solver.solver2(0))

if __name__ == "__main__":
    main()