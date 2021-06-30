#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 1:
            return 1
        a = sorted(envelopes, key=lambda x:(x[0],-x[1]))  #使用sorted函数可以对数组进行个性化排序,key=lambda x:(x[0],-x[1])
        n = len(envelopes)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if a[i][1]>a[j][1]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)
# @lc code=end

