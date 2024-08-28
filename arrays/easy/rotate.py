class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int], k: int):
        def brute_force(nums, k):
            def right_shift(arr):
                temp = arr[-1]
            
                for i in range(len(arr) - 1, -1, -1):
                    arr[i] = arr[i - 1]
            
                arr[0] = temp
            
                return arr

            for i in range(k):
                right_shift(nums)
        
            return nums
        
        #return brute_force(nums, k)
        
        def solution2(nums, k):
            if len(nums) == 1 or len(nums) == 0:
                return nums
        
            if k > len(nums):
                while k > len(nums):
                    k = k - len(nums)

            temp = nums[len(nums) - k : ]
            
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = nums[i - k]
            
            for i in range(len(temp)):
                nums[i] = temp[i]
            
            return nums
            
        return solution2(nums, k)
            
            
                

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,2,3,4,5,6,7], k = 3))
    print(solver.solver(nums = [-1,-100,3,99], k = 2))

if __name__ == "__main__":
    main()