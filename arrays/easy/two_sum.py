class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, target):
        """
        this is the brute force way:
        """
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        """
            A better approach is using a hashmap:
        """
        # first we add a each element's value as a key and its
        # index as the value:
        index_map = {}
        
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = i
        
        # next, we check if each element's complement is in the hash table:
        # but we need to make sure that the complement is not nums[i] itself:
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in index_map and index_map[complement] != i:
                return [i, index_map[complement]]
        
        return []

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,7,11,15], target = 9))
    print(solver.solver(nums = [3,2,4], target = 6))
    print(solver.solver(nums = [3,3], target = 6))

if __name__ == "__main__":
    main()