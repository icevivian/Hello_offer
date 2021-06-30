#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        table = [[] for j in range(numRows)]
        r = 0
        flag = 1
        for i in s:
            table[r].append(i)
            if r == numRows-1 or r == 0:
                flag = 1-flag
            if flag:
                r = r-1
            else:
                r = r+1
        res = ''
        for row in table:
            res = res+''.join(row)
        return res
# @lc code=end

