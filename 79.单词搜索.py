#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        visited = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]!=word[0]:
                    continue
                visited.append((i,j))
                if self.backtrace(i,j,visited,board,word):
                    return True
                visited.pop()
        return False

    def backtrace(self, row, col, visited, board, word):
        if len(visited)==len(word):
            return True
        index = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(4):
            newrow, newcol = row+index[i][0], col+index[i][1]
            if newrow<0 or newrow>=len(board) or newcol<0 or newcol>=len(board[0]) or (newrow,newcol) in visited or board[newrow][newcol]!=word[len(visited)]:
                continue
            visited.append((newrow,newcol))
            if self.backtrace(newrow, newcol, visited, board, word):
                return True
            visited.pop()                

# @lc code=end

