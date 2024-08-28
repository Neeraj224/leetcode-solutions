import math

class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(serlf, piles, h):
        # pass
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hoursSpent = 0
            
            for pile in piles:
                hoursSpent += math.ceil(pile / mid)
            
            if hoursSpent <= h:
                right = mid
            else:
                left = mid + 1
            
        return right

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(piles = [3,6,7,11], h = 8))
    print(solver.solver(piles = [30,11,23,4,20], h = 5))
    print(solver.solver(piles = [30,11,23,4,20], h = 6))

if __name__ == "__main__":
    main()