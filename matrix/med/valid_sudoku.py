from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, board):
        # pass
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r]) or \
                   (board[r][c] in cols[c]) or \
                   (board[r][c] in boxes[(r // 3, c // 3)]):
                       return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(board = \
        [["5","3",".",".","7",".",".",".","."] \
        ,["6",".",".","1","9","5",".",".","."] \
        ,[".","9","8",".",".",".",".","6","."] \
        ,["8",".",".",".","6",".",".",".","3"] \
        ,["4",".",".","8",".","3",".",".","1"] \
        ,["7",".",".",".","2",".",".",".","6"] \
        ,[".","6",".",".",".",".","2","8","."] \
        ,[".",".",".","4","1","9",".",".","5"] \
        ,[".",".",".",".","8",".",".","7","9"]]))
    print(solver.solver(board = \
        [["8","3",".",".","7",".",".",".","."] \
        ,["6",".",".","1","9","5",".",".","."] \
        ,[".","9","8",".",".",".",".","6","."] \
        ,["8",".",".",".","6",".",".",".","3"] \
        ,["4",".",".","8",".","3",".",".","1"] \
        ,["7",".",".",".","2",".",".",".","6"] \
        ,[".","6",".",".",".",".","2","8","."] \
        ,[".",".",".","4","1","9",".",".","5"] \
        ,[".",".",".",".","8",".",".","7","9"]]))
    # print(solver.solver())

if __name__ == "__main__":
    main()
