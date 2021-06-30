#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        track = []
        leftc, rightc = n, n
        self.backtrack(track, leftc, rightc)
        return [''.join(self.res[i]) for i in range(len(self.res))]
    
    def backtrack(self, track, leftc, rightc):
        if rightc < leftc or leftc<0 or rightc<0:
            return 
        if leftc ==0 and rightc == 0:
            self.res.append(list(track))
        # 尝试放入左括号
        track.append('(')
        self.backtrack(track, leftc-1, rightc)
        track.pop()
        # 尝试放入右括号
        track.append(')')
        self.backtrack(track, leftc, rightc-1)
        track.pop()               
            
# @lc code=end

