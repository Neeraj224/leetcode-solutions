class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, skill):
        # pass
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        
        master_list = []
        
        while left <= right:
            master_list.append([skill[left], skill[right]])
            left += 1
            right -= 1
        
        if master_list:
            product_sum = master_list[0][0] * master_list[0][1]
        else:
            return -1
        
        for i in range(1, len(master_list)):
            if master_list[i - 1][0] + master_list[i - 1][1] != master_list[i][0] + master_list[i][1]:
                return -1
            else:
                product_sum += master_list[i][0] * master_list[i][1]
        
        return product_sum
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(skill = [3,2,5,1,3,4]))
    print(solver.solver(skill = [3,4]))
    print(solver.solver(skill = [1,1,2,3]))

if __name__ == "__main__":
    main()