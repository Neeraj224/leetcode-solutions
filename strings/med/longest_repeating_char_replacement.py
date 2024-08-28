class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s, k):
        # pass
        countmap = {}
        
        left = 0
        maxfreq = 0
        
        for right in range(len(s)):
            # get() -> if it exists, get that value, else return 0 as the value:
            countmap[s[right]] = 1 + countmap.get(s[right], 0)
            
            maxfreq = max(maxfreq, countmap[s[right]])
            
            # if windowsize minus the frequency of the most common element
            # is greater than k, then we need to adjust our window size:
            if (right - left + 1) - maxfreq > k:
                countmap[s[left]] -= 1
                left += 1
            
        return (right - left + 1)
                
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "ABAB", k = 2))
    print(solver.solver(s = "AABABBA", k = 1))
    # print(solver.solver())

if __name__ == "__main__":
    main()