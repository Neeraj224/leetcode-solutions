class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, board):
        # pass
        playboard = [[0 for i in range(len(board[0]))] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                playboard[i][j] = board[i][j]
        
        for i in range(len(playboard)):
            for j in range(len(playboard[0])):
                if ((i == 0) or (j == 0) or (i == len(playboard) - 1) or (j == len(playboard[0]) - 1)) and playboard[i][j] == 'O':
                    playboard[i][j] = 'E'

        edgeboard = [[0 for i in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(playboard)):
            for j in range(len(playboard[0])):
                edgeboard[i][j] = playboard[i][j]

        def dfs(row, col):
            if playboard[row][col] == 'V':
                return
            
            if playboard[row][col] == 'X':
                playboard[row][col] = 'V'
                return
            
            playboard[row][col] = 'V'
            
            if playboard[row][col] == 'O':
                playboard[row][col] = 'E'
                
            if row - 1 >= 0:
                # up
                dfs(row - 1, col)
            if col + 1 < len(playboard[0]):
                # right
                dfs(row, col + 1)
            if row + 1 < len(playboard):
                # down
                dfs(row + 1, col)
            if col - 1 >= 0:
                # left
                dfs(row, col - 1)
            
        
        for i in range(len(playboard)):
            for j in range(len(playboard[0])):
                if playboard[i][j] == 'E':
                    dfs(i, j)

        for i in range(len(playboard)):
            for j in range(len(playboard[0])):
                if edgeboard[i][j] == 'E':
                    playboard[i][j] = 'O'
                else:
                    playboard[i][j] = 'X'
                    
        return playboard
                
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
    # print(solver.solver(board = [["X"]]))
    print(solver.solver([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))

if __name__ == "__main__":
    main()