#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[0 for i in range(n)] for j in range(n)]
        # dp[i][j]表示s[i...j]要成为回文串的最少插入次数
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=1+min(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
        
# @lc code=end

