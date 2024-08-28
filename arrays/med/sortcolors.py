class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        counts = dict()
        
        for color in nums:
            if color not in counts:
                counts[color] = 1
            else:
                counts[color] += 1
        
        keys = list(counts.keys())
        keys.sort()
        sorted_counts = { i: counts[i] for i in keys }
        
        for i in range(len(nums)):
            if 0 in sorted_counts:
                if sorted_counts[0]:
                    nums[i] = 0
                    sorted_counts[0] -= 1
                    continue
            
            if 1 in sorted_counts:
                if sorted_counts[1]:
                    nums[i] = 1
                    sorted_counts[1] -= 1
                    continue
            
            if 2 in sorted_counts:
                if sorted_counts[2]:
                    nums[i] = 2
                    sorted_counts[2] -= 1
                    continue
        
        return nums
                
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,0,2,1,1,0]))
    print(solver.solver(nums = [2,0,1]))
    print(solver.solver(nums = [1]))

if __name__ == "__main__":
    main()