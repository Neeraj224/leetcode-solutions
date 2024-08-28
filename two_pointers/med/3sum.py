class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        # pass
        triplets = set()
        nums.sort()
        
        # i will be our anchor point
        for i in range(len(nums) - 1):
            # after deciding our anchor point, this is just two-sum then:
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                
                if currentSum == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        
        return triplets
                

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [-1,0,1,2,-1,-4]))
    print(solver.solver(nums = [0,1,1]))
    print(solver.solver(nums = [0,0,0]))

if __name__ == "__main__":
    main()