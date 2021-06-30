#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[0] = 0
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    # 进阶：1.写出暴力解，即状态转移方程；
    #      2.使用备忘录，字典或者数组
    #      3.状态压缩，减少空间使用，例如这里每次都只需要存储dp[i-1]和dp[i-2]
# @lc code=end

