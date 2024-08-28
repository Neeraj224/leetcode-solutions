class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        
        # maxcount = float("-inf")
        # cmap = {}
        # count = 0
        # i = 0
        
        # while i < len(s):
        #     cmap[s[i]] = 1
        #     count += 1
        #     j = i + 1
            
        #     while j < len(s):
        #         if s[j] not in cmap:
        #             cmap[s[j]] = 1
        #             count += 1
        #         else:
        #             cmap = {}
        #             break
                    
        #         j += 1
                
        #     maxcount = max(maxcount, count)
        #     count = 0
        #     i += 1
        
        # return maxcount if maxcount != float("-inf") else 0

        charset = set()
        left = 0
        maxcount = float("-inf")
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            
            charset.add(s[right])
            
            maxcount = max(maxcount, right - left + 1)
        
        return maxcount if maxcount != float("-inf") else 0

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "abcabcbb"))
    print(solver.solver(s = "bbbbb"))
    print(solver.solver(s = "pwwkew"))
    print(solver.solver(s = "dvdf"))

if __name__ == "__main__":
    main()