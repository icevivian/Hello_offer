#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 动态规划
        n = len(s)
        dp = [0 for i in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            if int(s[i-1])!=0: # 第i个字符不为0时，可以单独组成一个编码
                dp[i]=dp[i]+dp[i-1]
            if int(s[i-2])!=0 and i>=2 and 10*int(s[i-2])+int(s[i-1])<=26: # 第i-1个字符不为0时，并且i-1和1组合起来<=26时，i-1和i可以组成一个编码
                dp[i]=dp[i]+dp[i-2]
        return dp[n] 
# @lc code=end

