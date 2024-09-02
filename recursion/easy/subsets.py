class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        # pass
        subsequences = []

        def generate(index, current):
            if index == len(nums):
                if current not in subsequences:
                    subsequences.append(current.copy())
                return
            
            if current not in subsequences:
                subsequences.append(current.copy())

            # take the element and see:
            current.append(nums[index])
            generate(index + 1, current)

            # now, move on with the next element,
            # so, dont take the element and see:
            current.pop()
            generate(index + 1, current)
        
        generate(0, [])

        return subsequences

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,2,3]))
    print(solver.solver(nums = [0]))
    # print(solver.solver())

if __name__ == "__main__":
    main()