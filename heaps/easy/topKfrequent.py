class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, k):
        # pass
        countmap = {}
        
        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                countmap[num] += 1
        
        #print(countmap)
        sorted_map = dict(sorted(countmap.items(), key = lambda item: item[1], reverse = True))
        # print(sorted_map)
        kfrequent = []
        
        for key, value in sorted_map.items():
            if k > 0:
                kfrequent.append(key)
                k -= 1
                
        return kfrequent

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,1,1,2,2,3], k = 2))
    print(solver.solver(nums = [1, 2], k = 1))
    # print(solver.solver())

if __name__ == "__main__":
    main()