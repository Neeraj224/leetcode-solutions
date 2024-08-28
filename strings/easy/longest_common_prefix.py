class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, strs):
        if strs[0][0] != strs[1][0]:
            return ""

        if len(strs) == 0:
            return ""
        
        res = strs[0]
        
        for i in range(1, len(strs)):
            while res != strs[i][:len(res)]:
                res = res[:-1]
                if res == "":
                    return ""

        return res
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(strs = ["flower","flow","flight"]))
    print(solver.solver(strs = ["dog","racecar","car"]))

if __name__ == "__main__":
    main()