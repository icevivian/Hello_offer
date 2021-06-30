#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minvalue = 10001
        for sell in range(1,len(prices)):
            minvalue = min(minvalue, prices[sell-1])
            res = max(res, prices[sell]-minvalue)
        return res


# @lc code=end

