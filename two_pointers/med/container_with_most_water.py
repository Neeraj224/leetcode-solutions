class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, height):
        # pass
        """
            Brute force approach:
                passes 52/62 cases before throwing TLE:
        """
        # max_height = float('-inf')
        
        # for i in range(0, len(height)):
        #     for j in range(i + 1, len(height)):
        #         if height[j] > height[i]:
        #             current_height = height[i]
        #         else:
        #             current_height = height[j]
        #         max_height = max((current_height * (j - i)), max_height)
        
        # return max_height
        """
            Two pointer approach:
        """
        left = 0
        right = len(height) - 1
        
        maxWater = float("-inf")
        
        while left < right:
            maxWater = max(maxWater, (min(height[left], height[right]) * (right - left)))
            
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        
        return maxWater
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(height = [1,8,6,2,5,4,8,3,7]))
    print(solver.solver(height = [1,1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()