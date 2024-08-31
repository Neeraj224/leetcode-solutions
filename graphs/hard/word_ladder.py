from collections import deque
# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.adjacencyList = {}
    
#     def addEdge(self, word):
#         left = 0
        
#         while left <= len(word) - 2:
#             if word[left] in self.adjacencyList:
#                 if word[left + 1] in self.adjacencyList[word[left]]:
#                     pass
#                 else:
#                     self.adjacencyList[word[left]].append(word[left + 1])
#             else:
#                 self.adjacencyList[word[left]] = []
#                 self.adjacencyList[word[left]].append(word[left + 1])
            
#             if word[left + 1] in self.adjacencyList:
#                 if word[left] in self.adjacencyList[word[left + 1]]:
#                     pass
#                 else:
#                     self.adjacencyList[word[left + 1]].append(word[left])
#             else:
#                 self.adjacencyList[word[left + 1]] = []
#                 self.adjacencyList[word[left + 1]].append(word[left])
#             left += 1
        
#     def printGraph(self):
#         for node in self.adjacencyList:
#             print(str(node) + ": " + str(self.adjacencyList[node]))
    
    
#     def bfs(self, src, dest):
#         queue = []
#         visited = set()
#         traversed = []
#         distance = 0
#         queue.append((src, distance))
#         traversed.append((src, distance))
        
#         while queue:
#             current, distance = queue.pop(0)
            
#             if self.adjacencyList[current] is not None:
#                 for neighbor in self.adjacencyList[current]:
#                     if neighbor == dest:
#                         return distance + 1
#                     if neighbor not in visited:
#                         traversed.append((neighbor, distance + 1))
#                         visited.add(neighbor)
#                         queue.append((neighbor, distance + 1))
        
#         return 0
              

class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, beginWord, endWord, wordList):
        # Create a set of all words in the word list for quick lookup.
        wordSet = set(wordList)

        # If endWord is not in the word list, return 0.
        if endWord not in wordSet:
            return 0

        # Use a queue to perform BFS (Breadth-First Search).
        wordQueue = deque([beginWord])

        # Distance from the beginWord (initially 1).
        distance = 1

        while wordQueue:
            size = len(wordQueue)
            distance += 1  # Increase distance at each level of BFS

            for _ in range(size):
                currWord = wordQueue.popleft()

                # Try changing each character of the current word
                for i in range(len(currWord)):
                    for j in range(26):  # Try all lowercase letters
                        temp = currWord[:i] + chr(ord('a') + j) + currWord[i+1:]

                        # If the new word matches the endWord, return the distance
                        if temp == endWord:
                            return distance

                        # If the new word is in the set, add it to the queue and remove it from the set
                        if temp in wordSet:
                            wordQueue.append(temp)
                            wordSet.remove(temp)

        # Return 0 if no transformation sequence is found
        return 0
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
    print(solver.solver(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
    print(solver.solver("a", "c", "abc"))

if __name__ == "__main__":
    main()