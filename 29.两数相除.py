#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 二分查找，dividend>divisor，n>=1
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        if dividend>=0 and divisor>0:
            return self.div(dividend,divisor)
        if dividend>=0 and divisor<0:
            return -self.div(dividend, -divisor)
        if dividend<0 and divisor>0:
            return -self.div(-dividend, divisor)
        return self.div(-dividend,-divisor)

    def div(self, a, b): # 递归，将分子逐渐缩小
        if a<b:
            return 0
        count = 1
        tb = b
        while tb+tb<=a:
            count = count+count
            tb = tb+tb
        return count+self.div(a-tb,b)
# @lc code=end

