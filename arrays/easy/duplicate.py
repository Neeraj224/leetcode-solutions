class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        """
            using a hashmap is a good and easy way
            but takes a lot of time i guess
        """
        # countmap = {}
        
        # for num in nums:
        #     if num in countmap:
        #         countmap[num] += 1
        #     else:
        #         countmap[num] = 1
        
        # for value in countmap.values():
        #     if value > 1:
        #         return True

        # return False
        """
            using a set is better:
        """
        seen_nums = set()
        
        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums.add(num)
        
        return False
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,2,3,1]))
    print(solver.solver(nums = [1,2,3,4]))
    print(solver.solver(nums = [1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()