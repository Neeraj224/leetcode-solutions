from collections import defaultdict
class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, strs):
        # sorted_strs = []
        # indices = []
        
        # for s in strs:
        #     sorted_strs.append(''.join(sorted(s)))
        
        # for i in range(len(sorted_strs)):
        #     if sorted_strs[i] == '#':
        #         continue

        #     current_word = sorted_strs[i]    
        #     current = []
        #     current.append(i)
            
        #     for j in range(i + 1, len(sorted_strs)):
        #         if sorted_strs[j] == "#":
        #             continue
        #         if sorted_strs[j] == current_word:
        #             current.append(j)
        #             sorted_strs[j] = "#"
            
        #     indices.append(current)
        
        # anagrams = []
        
        # for i in range(len(indices)):
        #     pattern = []
        #     for j in range(len(indices[i])):
        #         pattern.append(strs[indices[i][j]])
        #     anagrams.append(pattern)
        
        # return anagrams
        anagram_map = {}
        # print(anagram_map)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word].append(word)
            
        # print(anagram_map)
        return list(anagram_map.values())

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(solver.solver(strs = [""]))
    print(solver.solver(strs = ["a"]))

if __name__ == "__main__":
    main()